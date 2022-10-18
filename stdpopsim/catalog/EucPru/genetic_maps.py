import stdpopsim

_species = stdpopsim.get_species("EucPru")

_gm = stdpopsim.GeneticMap(
    species=_species,
    id="Pope_PSUv1",
    description="Genetic map inferred with twelve haploid bees from Colorado",
    long_description="""
        TODO
        """,
    url="DROPBOX TODO",
    sha256="TODO",
    file_pattern="genetic_map/eucera_pruinosa.{id}.hapmap.txt",
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
