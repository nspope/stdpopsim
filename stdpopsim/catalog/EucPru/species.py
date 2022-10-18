import stdpopsim
from . import genome_data


# Mean chromosomal rates
_recombination_rate_data = {
    "I": 3.1216265402124167e-11,
    "II": 3.529290802315087e-11,
    "III": 3.906598767640363e-11,
    "IV": 2.712098077556377e-11,
    "V": 2.4705737572511805e-11,
    "X": 2.9472374817864404e-11,
    "MtDNA": 0,
}

# Mutation rates
genomic_dna_mu = 1.84e-9
_mutation_rate_data = {
    "I": genomic_dna_mu,
    "II": genomic_dna_mu,
    "III": genomic_dna_mu,
    "IV": genomic_dna_mu,
    "V": genomic_dna_mu,
    "X": genomic_dna_mu,
    "MtDNA": 1.05e-7,
}

# Generic and chromosome-specific ploidy
# Species is haplodiploid, but stdpopsim doesn't support that
_species_ploidy = 2
_ploidy = {
    "I": _species_ploidy,
    "II": _species_ploidy,
    "III": _species_ploidy,
    "IV": _species_ploidy,
    "V": _species_ploidy,
    "X": _species_ploidy,
    "MtDNA": 1,
}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[], #FILLME
)
stdpopsim.utils.append_common_synonyms(_genome)

_species = stdpopsim.Species(
    id="EucPru",
    ensembl_id="FILLME",
    name="Eucera pruinosa",
    common_name="Hoary squash bee",
    genome=_genome,
    generation_time=1,
    population_size=20000, #eastern USA population
    ploidy=_species_ploidy,
    citations=[], #FILLME
)

stdpopsim.register_species(_species)
