from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from DB import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    project_name = Column(String, index=True)
    project_type = Column(String, index=True)
    classes = Column(String, index=True)

    owner = relationship("User", back_populates="projects")
    
    @staticmethod
    def Create(db: Session, project):
        db.add(project)
        db.commit()
        db.refresh(project)
        return project
