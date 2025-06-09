# app/db/crud.py
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional, Tuple, Any

from . import models  # models.py đã định nghĩa ở Giai đoạn 2
from app import schemas  # schemas.py đã định nghĩa ở Giai đoạn 2


# --- User CRUD ---
def get_user_by_id(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_role_name(db: Session, user_id: int) -> Optional[str]:
    user = db.query(models.User).options(joinedload(models.User.role)).filter(models.User.id == user_id).first()
    if user and user.role:
        return user.role.name
    return None


# --- Profile & Related CRUD ---
def get_user_profile_raw_data(db: Session, user_id: int) -> Optional[Tuple[
    models.User,
    Optional[models.Profile],
    Optional[models.Location],
    List[str],  # pet names
    List[str],  # interest names
    List[str],  # language names
    Optional[str],  # body_type_name
    Optional[str],  # orientation_name
    Optional[str],  # job_industry_name
    Optional[str],  # drink_status_name
    Optional[str],  # smoke_status_name
    Optional[str]  # education_level_name
]]:
    """
    Lấy toàn bộ thông tin thô của user cần thiết cho ML model,
    bao gồm cả việc join và tổng hợp từ các bảng liên quan.
    Trả về một tuple chứa các đối tượng model hoặc list of strings.
    """
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    profile = db.query(models.Profile).options(
        joinedload(models.Profile.body_type),
        joinedload(models.Profile.orientation),
        joinedload(models.Profile.job_industry),
        joinedload(models.Profile.drink_status),
        joinedload(models.Profile.smoke_status),
        joinedload(models.Profile.education_level)
    ).filter(models.Profile.user_id == user_id).first()

    location = db.query(models.Location).filter(models.Location.user_id == user_id).first()

    pets_q = db.query(models.Pet.name).join(models.UserPet).filter(models.UserPet.user_id == user_id).all()
    pet_names = [p[0] for p in pets_q]

    interests_q = db.query(models.Interest.name).join(models.UserInterest).filter(
        models.UserInterest.user_id == user_id).all()
    interest_names = [i[0] for i in interests_q]

    languages_q = db.query(models.Language.name).join(models.UserLanguage).filter(
        models.UserLanguage.user_id == user_id).all()
    language_names = [l[0] for l in languages_q]

    body_type_name = profile.body_type.name if profile and profile.body_type else None
    orientation_name = profile.orientation.name if profile and profile.orientation else None
    job_industry_name = profile.job_industry.name if profile and profile.job_industry else None
    drink_status_name = profile.drink_status.name if profile and profile.drink_status else None
    smoke_status_name = profile.smoke_status.name if profile and profile.smoke_status else None
    education_level_name = profile.education_level.name if profile and profile.education_level else None

    return (
        user,
        profile,
        location,
        pet_names,
        interest_names,
        language_names,
        body_type_name,
        orientation_name,
        job_industry_name,
        drink_status_name,
        smoke_status_name,
        education_level_name
    )


def get_all_other_user_ids_with_role(db: Session, current_user_id: int, role_name: str = "USER") -> List[int]:
    """
    Lấy ID của tất cả user khác có vai trò (role_name) cụ thể.
    """
    user_ids = db.query(models.User.id). \
        join(models.Role). \
        filter(models.Role.name == role_name, models.User.id != current_user_id). \
        all()
    return [uid[0] for uid in user_ids]


# --- Helper functions for reference tables (body_type, orientation, etc.) ---
# Bạn có thể thêm các hàm CRUD cho các bảng tham chiếu này nếu cần
# Ví dụ:
def get_body_type_by_name(db: Session, name: str) -> Optional[models.BodyType]:
    return db.query(models.BodyType).filter(models.BodyType.name == name).first()


# ... các hàm tương tự cho Orientation, JobIndustry, DrinkStatus, SmokeStatus, EducationLevel
# ... cũng như Pet, Interest, Language nếu bạn cần tạo mới chúng khi user nhập.

# --- Role CRUD (Ví dụ) ---
def get_role_by_name(db: Session, name: str) -> Optional[models.Role]:
    return db.query(models.Role).filter(models.Role.name == name).first()


def create_role(db: Session, role: schemas.user.RoleCreate) -> models.Role:  # Giả sử có RoleCreate schema
    db_role = models.Role(name=role.name, description=role.description)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role