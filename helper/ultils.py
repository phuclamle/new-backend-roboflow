def to_dict(obj):
    if not hasattr(obj, '__table__'):
        raise ValueError("The provided object is not a valid SQLAlchemy model instance.")
    
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}