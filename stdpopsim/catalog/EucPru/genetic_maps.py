import stdpopsim

_species = stdpopsim.get_species("EucPru")

_gm = stdpopsim.GeneticMap(
    species=_species,
    id="Pope_PSUv1",
    description="Genetic map inferred with twelve haploid bees from Colorado",
    long_description="""
    FILLME
    """,
    url="https://github.com/nspope/eucpru-popsim-data/raw/"
    "main/data/eucera_pruinosa.genetic_map.tar.gz",
    sha256="f7e50c9040f0a90a8138b473df30a04f6015874bd9227b4d5d36b54b0ce3e017",
    file_pattern="eucera_pruinosa.{id}.hapmap.txt",
    citations=[
        stdpopsim.Citation(
            author="FILLME",
            doi="FILLME",
            year=2023,
            reasons={stdpopsim.CiteReason.GEN_MAP},
        )
    ],
)
_species.add_genetic_map(_gm)
