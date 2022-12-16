import stdpopsim

_species = stdpopsim.get_species("EucPru")

_gm = stdpopsim.GeneticMap(
    species=_species,
    id="Pope_PSUv1",
    description="Genetic map inferred by pyrho with eight haploid bees from Puebla, Mexico",
    long_description="""
    FILLME
    """,
    url="https://sesame.uoregon.edu/~natep/eucpru-data/hapmap/"
    "eucera_pruinosa.pyrho.hapmap.tar.gz",
    sha256="807d3a5ea13909a7dd9cbf815dfeae9aee15c6fc9d95c5a1b031b936998c64b4",
    file_pattern="{id}.MEX.hapmap",
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
