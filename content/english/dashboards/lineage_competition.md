---
title: "SARS-CoV-2 Variant Competition"
description: "Estimates of SARS-CoV-2 variant frequencies and growth rate advantages from global SARS-CoV-2 genotype sequencing data"
banner: /dashboard_thumbs/lineage_competition.png
toc: true
plotly: true
menu:
  dashboard_menu:
    identifier: lineage_competition
    name: SARS-CoV-2 variant competition
dashboards_topics: [COVID-19, Infectious diseases]
data_status: "updating" # or "historic"

---
<div class="alert alert-info">All data last updated: {{< last_modified_lineage >}}</div>

SARS-CoV-2 is constantly evolving, with new variants competing against one another for domiance in different regions. This model integrates SARS-CoV-2 genotype sequencing data from around the world to estimate the growth advantage of different variants, which is then used to provide regional estimates of variant frequencies and how these are changing over time. This can be used by researchers who might wish to know which variants to focus on in their studies, or by public health officials who might wish to know which variants are likely to become dominant in their region.

The full set of model estimates can be found in the [GitHub repository](https://github.com/MurrellGroup/lineages).

## Global statistics on lineage competition

### Advantage estimates

Growth rate advantages are estimated from all variant frequency data, globally. A variant with a higher growth rate advantage is expected to increase in frequency relative to other variants.

<figure><img alt="Growth advantage estimates for the top variants" width="1000" src="https://raw.githubusercontent.com/MurrellGroup/lineages/main/plots/pruned_lineages_MCMC_lineage_growths.svg"></figure>

For convergent mutations (occuring independently at least three times), we estimate the contribution to growth rate advantage of each mutation.

<figure><img alt="Estimates of contribution to growth of convergently occuring mutations" width="1000" src="https://raw.githubusercontent.com/MurrellGroup/lineages/main/plots/N_MCMC_mutations.svg"></figure>

The relatedness of SARS-CoV-2 variants, with their estimated growth rate advantages, can be visualized in a phylogenetic tree. We show only recent variants, and key ancestral variants, and we exclude lineage with low growth rate estimates.

<figure><img alt="Growth-annotated phylogeny" width="1000" src="https://raw.githubusercontent.com/MurrellGroup/lineages/main/plots/tree_pruned.svg"></figure>

### Variant trajectories

The "model average" variant frequencies are forecasts from the model with all region-specific effects set to zero. This provides a single "snapshot" of the global variant situation. This is not meant to representative of the true global variant frequencies, since it is influenced by different sequencing coverage in different regions, but it is useful to understand the model's estimates of how quickly one variant might be expected to replace others.

Variants are colored such that related variants should be similar in color.

<figure><img alt="Model average variant trajectories" width="1000" src="https://raw.githubusercontent.com/MurrellGroup/lineages/main/plots/variant_trajectories_model_avg.svg"></figure>

<figure><img alt="Model average variant frequencies" width="1000" src="https://raw.githubusercontent.com/MurrellGroup/lineages/main/plots/muller_trajectories_model_avg.svg"></figure>

## Results from Sweden

We always include estimates of variant frequencies and growth rate advantages for Sweden. Swedish genotype data comes, as with all other data, from GISAID. Note that sequencing volumes are often low, especially when case counts themselves are low (and there are not many infections to sequence), and in such cases the estimates for variant frequencies in Sweden can be very uncertain.

<figure><img alt="SARS-CoV-2 genotype volumes" width="1000" src="https://raw.githubusercontent.com/MurrellGroup/lineages/main/plots/sequence_volume_Sweden.svg"></figure>

<figure><img alt="Variant trajectories in Sweden" width="1000" src="https://raw.githubusercontent.com/MurrellGroup/lineages/main/plots/variant_trajectories_Sweden.svg"></figure>

<figure><img alt="Variant frequencies in Sweden" width="1000" src="https://raw.githubusercontent.com/MurrellGroup/lineages/main/plots/muller_trajectories_country_Sweden.svg"></figure>

## Methods

Lineage dynamics are modelled using a Bayesian multinomial logistic regression over lineage counts. The latest global [GISAID](https://gisaid.org/) SARS-CoV-2 dataset (obtained via bulk download) is filtered to include only sequences with collection dates within the last 100 days. Lineage assignment is performed using [NextClade](https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli/index.html), retaining sequences with a “good” overall QC status, and >90% coverage. Daily lineage counts are aggregated by region (including only countries with sufficient recent sequencing volumes), with low-frequency sub-lineages (too rare to model) merged into their most recent ancestors.

Growth rates are modelled with a hierarchical approach. Each lineage's growth rate in a given region is the sum of a global rate and a region-specific random effect. The global rate for each lineage comprises three components: i) branch-specific terms for each branch ancestral to the lineage, ii) terms for convergent spike mutations occurring 3 or more times independently that are present in the lineage, and iii) a lineage-specific term. This parameterization allows for shared evidence when mutations occur across multiple branches, and phylogenetic heritability of growth rates, such that growth rates for closely-related lineages are more likely, under the model’s prior, to be similar to one another. Recombinants inherit weighted mixtures of their multiple parents' growth terms. Lineage-specific intercept terms, which contorl the relative timing of the emergence of variants, comprise a global shared term and region-specific random effects.

Gaussian priors (centered on zero) are used for each parameter type, with Gaussian hyperpriors over the log of their standard deviations. Posterior distributions are jointly sampled (for global and local parameters for all global data) using Hamiltonian Monte Carlo with the No-U-Turn sampler, implemented in [Julia's](https://julialang.org/) [AdvancedHMC.jl](https://github.com/TuringLang/AdvancedHMC.jl) package.

For all plots, we use the [Pango designations](https://github.com/cov-lineages/pango-designation/) for lineage names.

We gratefully acknowledge all data contributors, i.e. the Authors and their Originating Laboratories responsible for obtaining the specimens, and their Submitting Laboratories that generated the genetic sequence and metadata and shared via the GISAID Initiative the data on which this research is based.