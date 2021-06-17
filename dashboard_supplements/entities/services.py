from types import SimpleNamespace

from dashboard_supplements.demo_text.demo_dashboard_text import (
    business_label_mapper,
    persona_names_label_mapper,
    property_label_mapper,
    sample_business_names,
    sample_persona_names,
    sample_property_names,
)


class ServiceCategory:
    def __init__(
        self,
        sample_information: list,
        select_prompt_specification: str,
        image_path: str,
        display_label_mapper: dict,
    ) -> None:
        self.sample_information = sample_information
        self.prompt = select_prompt_specification
        self.image_path = image_path
        self.display_label_mapper = display_label_mapper


personal_service_category = ServiceCategory(
    sample_information=sample_persona_names,
    select_prompt_specification="policy holder",
    image_path="demo_persona_photos",
    display_label_mapper=persona_names_label_mapper,
)

property_service_category = ServiceCategory(
    sample_information=sample_property_names,
    select_prompt_specification="property",
    image_path="demo_property_photos",
    display_label_mapper=property_label_mapper,
)

business_service_category = ServiceCategory(
    sample_information=sample_business_names,
    select_prompt_specification="business",
    image_path="demo_business_photos",
    display_label_mapper=business_label_mapper,
)

service_names = SimpleNamespace(
    pfr="PFR",
    life_events="LifeEvents",
    property_details="PropertyDetails",
    property_risks="PropertyRisks",
    auto_prefill="AutoPrefill",
    life_prefill="LifePrefill",
    property_replacement="PropertyReplacement",
    smb="SMB",
)

service_category_mapper = {
    service_names.pfr: personal_service_category,
    service_names.life_events: personal_service_category,
    service_names.life_prefill: personal_service_category,
    service_names.auto_prefill: personal_service_category,
    service_names.smb: business_service_category,
    service_names.property_details: property_service_category,
    service_names.property_risks: property_service_category,
    service_names.property_replacement: property_service_category,
}
