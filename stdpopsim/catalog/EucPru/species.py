import stdpopsim
from . import genome_data

# Mean chromosomal rates
_recombination_rate_data = {
    "epru001": 1.5771138601144577e-08,
    "epru002": 1.7185422948290452e-08,
    "epru003": 1.5315251175509008e-08,
    "epru004": 1.7680777364083655e-08,
    "epru005": 1.9220909060076074e-08,
    "epru006": 1.8370825433302474e-08,
    "epru007": 2.0121180700429858e-08,
    "epru008": 2.143449558088746e-08,
    "epru009": 1.9103364466958788e-08,
    "epru010": 2.3931215807195916e-08,
    "epru011": 1.878019022814945e-08,
    "epru012": 2.2149475705908217e-08,
    "epru013": 2.4024726362802502e-08,
    "epru014": 2.4843306853158356e-08,
    "epru015": 2.4415380465386215e-08,
    "epru016": 2.917706468022998e-08,
    "epru017": 3.2662694421565e-08,
    "epru018": 3.1480526128089325e-08,
    "epru019": 3.3275098605608576e-08,
    "epru020": 2.7796405775025306e-08,
    "epru021": 3.2349940581986494e-08,
    "epru022": 3.095768553783235e-08,
    "epru023": 1.0882932228564097e-10,
}

# Mutation rates
_autosomal_mu = 6.02e-9
_mutation_rate_data = {k: _autosomal_mu for k in _recombination_rate_data.keys()}

# Generic and chromosome-specific ploidy
# Species is haplodiploid, but stdpopsim doesn't support that
# As males were sequenced for model fitting, use haploids
_species_ploidy = 1
_ploidy = {k: _species_ploidy for k in _recombination_rate_data.keys()}

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
