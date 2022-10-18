import stdpopsim

_species = stdpopsim.get_species("EucPru")

# exons
_an = stdpopsim.Annotation(
    species=_species,
    id="FlyBase_BDGP6.32.51_exons",
    description="FlyBase exon annotations on BDGP6",
    url=("TODO GFF"),
    gff_sha256="TODO",
    intervals_url=("TODO BED"),
    intervals_sha256="TODO",
    citations=[], #FILLME
    file_pattern="annotations/eucera_pruinosa.exons.{id}.bed",
    annotation_source="FILLME",
    annotation_type="exon",
)
_species.add_annotations(_an)
