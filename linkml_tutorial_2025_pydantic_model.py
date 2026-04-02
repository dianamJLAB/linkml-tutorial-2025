from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'https://w3id.org/dmlinkml/tutorial/2025/schema/',
     'description': 'This is a data model for representing plant tissue samples, '
                    'which are a specific type of sample that can be collected and '
                    'analyzed in various scientific fields. The data model '
                    'includes classes, enums, and slots that capture relevant '
                    'information about plant tissue samples, such as their unique '
                    'identifiers, names, descriptions, storage containers, plate '
                    'locations, ploidy levels, and collection date and time. The '
                    'model also includes mappings to external ontologies to '
                    'enhance interoperability and integration with other datasets '
                    'and ontologies in the domain of plant biology and related '
                    'fields.',
     'id': 'https://w3id.org/dmlinkml/tutorial/2025/schema',
     'imports': ['linkml:types'],
     'license': 'CC-BY-4.0',
     'name': 'linkml_tutorial_2025_dm',
     'prefixes': {'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'NCBITaxon': {'prefix_prefix': 'NCBITaxon',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'PO': {'prefix_prefix': 'PO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/PO_'},
                  'SIO': {'prefix_prefix': 'SIO',
                          'prefix_reference': 'http://semanticscience.org/resource/SIO_'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'https://w3id.org/dmlinkml/tutorial/2025/schema/example/'},
                  'link_ml_tutorial_2025': {'prefix_prefix': 'link_ml_tutorial_2025',
                                            'prefix_reference': 'https://w3id.org/dmlinkml/tutorial/2025/schema/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'obo': {'prefix_prefix': 'obo',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'src/dmlinkml/schema/linkml_tutorial_2025.yaml'} )

class SampleContainerEnum(str, Enum):
    """
    An enumeration of different types of containers that can be used to store samples, such as vials, tubes, petri dishes, etc.
    """
    vial = "vial"
    """
    A small container typically used to hold liquid samples.
    """
    tube = "tube"
    """
    A cylindrical container often used for storing and transporting samples, especially in laboratory settings.
    """
    plate = "plate"
    """
    A flat container with multiple wells or compartments, commonly used for culturing cells or conducting experiments  in a laboratory.
    """
    SNOMEDCOLON409990004 = "SNOMED:409990004"
    """
    Petri Dish from SNOMED CT ontology: A shallow, circular dish with a lid, typically used for culturing microorganisms  or small plants in a laboratory setting.
    """


class NCBITaxonEnum(str):
    pass


class TissueTypeEnum(str):
    pass


class PloidyEnum(str, Enum):
    """
    An enumeration of different ploidy levels, which refer to the number of sets of chromosomes present in the cells of an organism.  Common ploidy levels include haploid (one set of chromosomes), diploid (two sets of chromosomes), triploid (three sets of chromosomes), etc.
    """
    haploid = "haploid"
    """
    A ploidy level where there is only one set of chromosomes present in the cells.
    """
    diploid = "diploid"
    """
    A ploidy level where there are two sets of chromosomes present in the cells.
    """
    triploid = "triploid"
    """
    A ploidy level where there are three sets of chromosomes present in the cells.
    """
    tetraploid = "tetraploid"
    """
    A ploidy level where there are four sets of chromosomes present in the cells.
    """
    allapolyploid = "allapolyploid"
    """
    A ploidy level where there are multiple sets of chromosomes that are derived from different species, often as a result of hybridization events.
    """



class Sample(ConfiguredBaseModel):
    """
    A sample is a portion, piece, or segment that is representative of a whole. It is often used in various fields such as science, statistics, and marketing to gather information or make inferences about a larger population or phenomenon. A sample can be collected, analyzed, and studied to draw conclusions or make predictions about the entire group it represents.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/dmlinkml/tutorial/2025/schema'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'slot_uri': 'schema:description'} })
    sample_container: SampleContainerEnum = Field(default=..., description="""The container in which the sample is stored, such as a vial, tube, plate, or petri dish.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })


class PlantTissueSamples(Sample):
    """
    Plant tissue sample is a sample taken from a plant tissue, which is a group of cells that perform a specific function in the plant.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['psample',
                     'plant_sample',
                     'plant_tissue_sample',
                     'planttissue',
                     'ptiss'],
         'broad_mappings': ['NCIT:C19697'],
         'from_schema': 'https://w3id.org/dmlinkml/tutorial/2025/schema'})

    tissue_type: TissueTypeEnum = Field(default=..., description="""The type of plant tissue from which the sample was taken, such as leaf, root, stem, flower, etc. This information can be important for understanding the biological context of the sample and for conducting analyses that are specific to certain tissue types. The tissue type can also provide insights into the functions and characteristics of the sample, as different plant tissues have different roles and properties within the plant organism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSamples']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'slot_uri': 'schema:description'} })
    sample_container: SampleContainerEnum = Field(default=..., description="""The container in which the sample is stored, such as a vial, tube, plate, or petri dish.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Sample.model_rebuild()
PlantTissueSamples.model_rebuild()
