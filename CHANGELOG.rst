-------------------------
[0.2.0-beta] - 2022-XX-XX
-------------------------

TODO release note summary here

**Bug fixes**:

TODO

**New species**:

TODO check against #1230
https://github.com/popsim-consortium/stdpopsim/issues/1230

- Aedes aegypti (:user:`manolofperez`, :pr:`871`).
  QC'd by :user:`petrelharp`, :pr:`893`.

- Anas platyrhynchos (:user:`petrelharp`, :pr:`826`).
  QC'd by :user:`igronau`, :pr:`1070`.

- Anolis carolinensis (:user:`vcaudill`, :pr:`874`).
  QC'd by :user:`andrewkern`, :pr:`896`.

- Anopheles gambiae (:user:`andrewkern`, :pr:`856`).
  QC'd by :user:`petrelharp`, :pr:`906`.

- Apis mellifera (:user:`janaobsteter`, :pr:`1025`).
  QC'd by :user:`manolofperez`, :pr:`1268`.

- Bos taurus (:user:`grahamgower`, :pr:`600`).
  QC'd by :user:`gtsambos`, :pr:`1269`.

- Caenorhabditis elegans (:user:`attrna`, :pr:`910`).
  QC'd by :user:`chriscrsmith`, :pr:`1265`.

- Chlamydomonas reinhardtii (:user:`aays`, :pr:`863`).
  QC'd by :user:`izabelcavassim`, :pr:`1067`.

- Drosophila sechellia (:user:`jradrion`, :pr:`872`).
  QC'd by :user:`vitorpavinato`, :pr:`1264`.

- Gasterosteus aculeatus (:user:`vitorpavinato`, :pr:`1105`).
  QC'd by :user:`manolofperez`, :pr:`1253`.

- Helianthus annuus (:user:`chriscrsmith`, :pr:`1218`).
  QC'd by :user:`xin-huang`, :pr:`1250`.

- Heliconius melpomene (:user:`percyfal`, :pr:`870`).
  QC'd by :user:`noscode`, :pr:`1165`.

- Pan troglodytes (:user:`xin-huang`, :pr:`1215`).
  QC'd by :user:`janaobsteter`, :pr:`1291`.

- Papio anubis (:user:`saurabhbelsare`, :pr:`1216`).
  QC'd by :user:`mufernando`, :pr:`1263`.

- Streptococcus agalactiae (:user:`jeanrjc`, :pr:`854`).
  QC'd by :user:`vitorpavinato`, :pr:`1251`.

**New models**:

- AnaPla/MallardBlackDuck_2L19 (:user:`petrelharp`, :pr:`883`).
  QC'd by :user:`igronau`, :pr:`1021`.

- AnoGam/GabonAg1000G_1A17 (:user:`andrewkern`, :pr:`856`).
  QC'd by :user:`petrelharp`, :pr:`1279`.

- BosTau/HolsteinFriesian_1M13 (:user:`grahamgower`, :pr:`600`).
  QC'd by :user:`igronau`, :pr:`1272`.

- HomSap/OutOfAfricaExtendedNeandertalAdmixturePulse_3I21
  (:user:`leonardolasi`, :pr:`1066`).
  QC'd by :user:`awohns`, :pr:`1259`.

- HomSap/OutOfAfrica_4J17 (:user:`rwaples`, :pr:`726`).
  QC'd by :user:`jeffspence`, :pr:`1246`.

- HomSap/Africa_1B08 (:user:`izabelcavassim`, :pr:`993`).
  QC'd by :user:`petrelharp`, :pr:`995`.

- HomSap/AncientEurope_4A21 (:user:`alipearson`, :pr:`941`).
  QC'd by :user:`mufernando`, :pr:`1256`.

- PapAnu/SinglePopSMCpp_1W22 (:user:`saurabhbelsare`, :pr:`1216`).
  QC'd by :user:`attrna`, :pr:`1261`.

**New genetic maps**:

- CaeEle/RockmanRIAIL_ce11 (:user:`attrna`, :pr:`910`).

- DroMel/ComeronCrossoverV2_dm6 liftover (:user:`grahamgower`, :pr:`592`).

- HomSap/HapMapII_GRCh38 liftover (:user:`saurabhbelsare`, :pr:`1301`).

- HomSap/DeCodeSexAveraged_GRCh38 liftover (:user:`saurabhbelsare`, :pr:`XXX`).

- HomSap/PyrhoXXX_GRCh38 (:user:`jeffspence`, :pr:`572` and :pr:`575`),
  for XXX in ACB, ASW, BEB, CDX, CEU, CHB, CHS, CLM, ESN, FIN, GBR, GIH, GWD,
  IBS, ITU, JPT, KHV, LWK, MSL, MXL, PEL, PJL, PUR, STU, TSI, and YRI.

**New features**:

TODO preliminary list, look over PRs
- Simulation
  - gene conversion (#1106, needs docs?)
  - DFEs (#462, #588, #584)
  - sweeps/trajectory conditioning (#462, others)
- Infrastructure
  - Annotation class (#560)
  - DFE class (#1002)
  - MutationType class
- Catalog development
  - automate species addition (#790)
  - assembly liftover (#574)

**New annotations**:

- AraTha/araport_11 (:user:`XXX`, :pr:`XXX`).
  QC'd by :user:`XXX`, :pr:`XXX`.

- DroMel/FlyBase_BDGP6.32.51 (:user:`XXX`, :pr:`XXX`).
  QC'd by :user:`XXX`, :pr:`XXX`.

- HomSap/ensembl_havana_104 (:user:`XXX`, :pr:`XXX`).
  QC'd by :user:`XXX`, :pr:`XXX`.

**New DFEs**:

- DroMel/Gamma_H17 (:user:`XXX`, :pr:`XXX`).
  QC'd by :user:`XXX`, :pr:`XXX`.

- DroMel/LognormalPlusPositive_R16 (:user:`XXX`, :pr:`XXX`).
  QC'd by :user:`XXX`, :pr:`XXX`.

- HomSap/Gamma_K17 (:user:`XXX`, :pr:`XXX`).
  QC'd by :user:`XXX`, :pr:`XXX`.

- HomSap/Gamma_H17 (:user:`XXX`, :pr:`XXX`).
  QC'd by :user:`XXX`, :pr:`XXX`.

**Additions to CLI**:

TODO

**Additions to documentation**:

TODO

--------------------
[0.1.2] - 2020-05-29
--------------------

Important bugfix and feature release, recommended for all users.

Significant errors in the HomSap/OutOfAfrica_3G09 and HomSap/OutOfAfrica_2T12
models have been fixed. **We recommend repeating any analyses performed using
these models**. See `here
<https://github.com/jeromekelleher/msprime-model-errors>`__ for more details on
the error in the three population Out of Africa model and analysis of the
differences from the correct model.

The recombination rate for AraTha was also off by a factor of 10.
**We recommend repeating any analyses performed using this species**.

**Bug fixes**:

- Fix error in HomSap/OutOfAfrica_3G09 model, in which migration between
  ancestral African and European populations was allowed to continue in the
  most ancient time period (:user:`apragsdale`, :pr:`496`, :issue:`516`).

- Fix similar error in HomSap/OutOfAfrica_2T12 model
  (:user:`ndukler`, :pr:`520`, :issue:`516`).

- Fix recombination rate estimate for AraTha (:user:`grahamgower`,
  :issue:`537`, :pr:`527`), which was off by a factor of 10.

- Require attrs >=19.10 (:user:`grahamgower`, :pr:`399`, :issue:`394`)

**New species**:

- Canis familiaris (:user:`grahamgower`, :pr:`375`).

- Pongo abelii (:user:`apragsdale`, :pr:`363`).

**New models**:

- HomSap/PapuansOutOfAfrica_10J19 model (:user:`grahamgower`, :pr:`372`).
  QC'd by :user:`noscode`, :pr:`387`.

- HomSap/AshkSub_7G19 model (:user:`agladstein`, :pr:`494`).
  QC'd by :user:`ndukler`, :pr:`536`.

**New features**:

- SLiM simulation engine (:user:`grahamgower`, :pr:`409`, plus numerous others.
  See e.g. :issue:`132` and :issue:`133` for background.)

- Support for DTWF, SMC, and SMC' models in msprime engine
  (:user:`grahamgower`, :pr:`398`, :issue:`392`).

- Warnings for users running simulations on non-autosomes
  (:user:`grahamgower`, :pr:`407`).

- Migrate all genetic map data to AWS (:user:`ndukler`, :pr:`514`, :issue:`335`)

- Warnings for users running simulations on non QC'd models
  (:user:`grahamgower`, :pr:`525`).

- Add `generation_time` (default=1) attribute to generic models
  (:user:`grahamgower`, :pr:`477`, :issue:`471`).

- Various documentation and citation improvements.

**Breaking changes**:

- Move the --quiet/-q command line option to the top-level. Previously
  we would write ``stdpopsim HomSap -q 10`` whereas we now write
  ``stdpopsim -q HomSap``. (:user:`jeromekelleher`, :issue:`515`, :pr:`547`)

- The long form ``--verbosity`` argument has been changed to ``--verbose``
  (:pr:`547`).

- Removed DroMel chrM (:user:`grahamgower`, :pr:`528`, :issue:`405`).

--------------------
[0.1.1] - 2020-01-02
--------------------

Bugfix release. Fixes some distribution issues and temporarily removes the
PonPyg species.

**Bug fixes**:

- Pin the msprime and attrs packages to resolve some distribution problems
  (:issue:`366`; :user:`jgallowa07` and :user:`gtsambos`).

**New features**:

- Provide citations for the genome assembly (:issue:`359`, :pr:`360`;
  :user:`andrewkern` and :user:`grahamgower`).

**Breaking changes**:

- Temporarily remove the PonPyg species from the catalog to provide time
  to fix issues with genomes and multi-species models (:issue:`365`).

--------------------
[0.1.0] - 2019-12-18
--------------------

Initial release.
