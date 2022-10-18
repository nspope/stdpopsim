import msprime
import numpy as np
import stdpopsim

_species = stdpopsim.get_species("EucPru")

class _GenomewideBootstrap:
    populations = [
        stdpopsim.Population(
            id="AZ",
            description="Eucera pruinosa population from Tucson, Arizona",
        ),
        stdpopsim.Population(
            id="CO",
            description="Eucera pruinosa population from Monterose, Colorado",
        ),
        stdpopsim.Population(
            id="MX",
            description="Eucera pruinosa population from Puebla, Mexico",
        ),
        stdpopsim.Population(
            id="PA",
            description="Eucera pruinosa population from State College, Pennsylvania",
        ),
    ]

    #TODO
    num_replicates = ...
    times = ...
    sizes = ...
    mergers = ...

    @staticmethod
    def _make_msprime_demography(sizes):
        #TODO
        demographic_events = []
        for sz, t in zip(sizes, times):
            demographic_events.append(
                msprime.PopulationParametersChange(time=t, initial_size=sz, population_id=0)
            )

    @staticmethod
    def generate_model(replicate):
        return stdpopsim.DemographicModel(
            id=f"NAExpansionGenomewide_4P23_{replicate}",
            description=f"Expansion across North America inferred using genome-wide genealogies, bootstrap replicate {replicate}"
            long_description="""
            FILLME
            """,
            populations=self.populations,
            citations=[], #FILLME
            generation_time=1,
            mutation_rate=1.29e-9,
            demographic_events=demographic_events,
            population_configurations=[
                msprime.PopulationConfiguration(metadata=pop.asdict())
                for pop in self.populations
            ],
        )

for i in range(_GenomewideBootstrap.num_replicates):
    _species.add_demographic_model(_GenomewideBootstrap.generate_model(i))
