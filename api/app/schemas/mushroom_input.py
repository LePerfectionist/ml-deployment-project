from pydantic import BaseModel, Field

class MushroomInput(BaseModel):
    cap_shape: str = Field(..., alias="cap-shape")
    cap_surface: str = Field(..., alias="cap-surface")
    cap_color: str = Field(..., alias="cap-color")
    bruises: str
    odor: str
    gill_attachment: str = Field(..., alias="gill-attachment")
    gill_spacing: str = Field(..., alias="gill-spacing")
    gill_size: str = Field(..., alias="gill-size")
    gill_color: str = Field(..., alias="gill-color")
    stalk_shape: str = Field(..., alias="stalk-shape")
    stalk_root: str = Field(..., alias="stalk-root")
    stalk_surface_above_ring: str = Field(..., alias="stalk-surface-above-ring")
    stalk_surface_below_ring: str = Field(..., alias="stalk-surface-below-ring")
    stalk_color_above_ring: str = Field(..., alias="stalk-color-above-ring")
    stalk_color_below_ring: str = Field(..., alias="stalk-color-below-ring")
    veil_type: str = Field(..., alias="veil-type")
    veil_color: str = Field(..., alias="veil-color")
    ring_number: str = Field(..., alias="ring-number")
    ring_type: str = Field(..., alias="ring-type")
    spore_print_color: str = Field(..., alias="spore-print-color")
    population: str
    habitat: str

    class Config:
        allow_population_by_field_name = True