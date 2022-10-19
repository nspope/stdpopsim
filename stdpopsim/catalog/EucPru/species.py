import stdpopsim
from . import genome_data

# Mean chromosomal rates
_recombination_rate_data = {
    "epru001": 8.787428352846912e-09,
    "epru002": 8.947178335866877e-09,
    "epru003": 7.950127522373918e-09,
    "epru004": 1.1298240324938394e-08,
    "epru005": 8.924378962336754e-09,
    "epru006": 9.960067918007561e-09,
    "epru007": 6.774029698872606e-09,
    "epru008": 1.121671324705038e-08,
    "epru009": 9.438375361917818e-09,
    "epru010": 1.2700783270622791e-08,
    "epru011": 9.522084927196391e-09,
    "epru012": 9.792412099723955e-09,
    "epru013": 1.0169779818816786e-08,
    "epru014": 8.25989238733627e-09,
    "epru015": 9.717368836682175e-09,
    "epru016": 9.430428070860897e-09,
    "epru017": 1.3148465910940151e-08,
    "epru018": 2.066099293636479e-08,
    "epru019": 1.255844906408334e-08,
    "epru020": 9.69322270891954e-09,
    "epru021": 1.9010622053037335e-08,
    "epru022": 2.1233903642383725e-08,
    "epru023": 5.7334586218694335e-08,
}

# Mutation rates
_autosomal_mu = 1.26e-9
_mutation_rate_data = {k: _autosomal_mu for k in genome_data.data}

# Generic and chromosome-specific ploidy
# Species is haplodiploid, but stdpopsim doesn't support that
_species_ploidy = 2
_ploidy = {k: _species_ploidy for k in genome_data.data}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate_data,
    mutation_rate=_mutation_rate_data,
    ploidy=_ploidy,
    citations=[],  # FILLME
)
stdpopsim.utils.append_common_synonyms(_genome)

_species = stdpopsim.Species(
    id="EucPru",
    ensembl_id="FILLME",
    name="Eucera pruinosa",
    common_name="Hoary squash bee",
    genome=_genome,
    generation_time=1,
    population_size=10000,  # ~eastern USA population
    ploidy=_species_ploidy,
    citations=[],  # FILLME
)

stdpopsim.register_species(_species)
