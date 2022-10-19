import stdpopsim

_species = stdpopsim.get_species("EucPru")

# exons
_an = stdpopsim.Annotation(
    species=_species,
    id="Pope_PSUv1_exons",
    description="Exon annotations from Eucera pruinosa genome assembly"
    "from Pope et al 2023",
    url=(
        "https://github.com/nspope/eucpru-popsim-data/raw/"
        "main/data/eucera_pruinosa.annotation.gff3.gz"
    ),
    gff_sha256="72ceaeff9e60806928f72238f31f9af22b83843f7028ee93b7d56a20b1fb7b89",
    intervals_url=(
        "https://github.com/nspope/eucpru-popsim-data/raw/"
        "main/data/eucera_pruinosa.annotation.tar.gz"
    ),
    intervals_sha256="bb4d28beacbe9491490854893feddfa750cdd8058105e585ca464160b2c14730",
    citations=[],  # FILLME
    file_pattern="eucera_pruinosa.{id}.exons",
    annotation_source="FILLME",
    annotation_type="exon",
)
_species.add_annotations(_an)

# not really an annotation, but a missing data mask
_mask = stdpopsim.Annotation(
    species=_species,
    id="Pope_PSUv1_mask",
    description="Missing data mask for Eucera pruinosa population"
    "genomics analyses from Pope et al 2023",
    url=(
        "https://github.com/nspope/eucpru-popsim-data/raw/"
        "main/data/eucera_pruinosa.mask.tar.gz"
    ),  # not a gff
    gff_sha256="774e3c5503281052f6d47570bdcbdd3f1e57c271728b6ed8545ee2aee379d73b",
    intervals_url=(
        "https://github.com/nspope/eucpru-popsim-data/raw/"
        "main/data/eucera_pruinosa.mask.tar.gz"
    ),
    intervals_sha256="774e3c5503281052f6d47570bdcbdd3f1e57c271728b6ed8545ee2aee379d73b",
    citations=[],  # FILLME
    file_pattern="eucera_pruinosa.{id}.mask",
    annotation_source="FILLME",
    annotation_type="missing_data",
)
_species.add_annotations(_mask)
