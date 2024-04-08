from pydantic import Field, BaseModel


class GPSDeviceCreateModel(BaseModel):
    """
        GPSDeviceCreateModel represents a write model to create a GPSDevice
    """
    name: str = Field(min_length=1, max_length=255)
