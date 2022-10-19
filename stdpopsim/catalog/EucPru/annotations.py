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
    intervals_sha256="28e10dac3984d9a1266a878e5e4886964cb63dbd0ad47d0687aa460b59b1df6c",
    citations=[],  # FILLME
    file_pattern="annotations/eucera_pruinosa.{id}.exons.bed",
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
    gff_sha256="9eaa1caf91688a44be25ce7c27adcabecba51194ebfd041a8752bb227483d689",
    intervals_url=(
        "https://github.com/nspope/eucpru-popsim-data/raw/"
        "main/data/eucera_pruinosa.mask.tar.gz"
    ),
    intervals_sha256="9eaa1caf91688a44be25ce7c27adcabecba51194ebfd041a8752bb227483d689",
    citations=[],  # FILLME
    file_pattern="annotations/eucera_pruinosa.{id}.mask.bed",
    annotation_source="FILLME",
    annotation_type="missing_data",
)
_species.add_annotations(_mask)
