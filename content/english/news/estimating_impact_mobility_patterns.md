---
title: Bayesian model for estimating the impact of mobility patterns on COVID-19 infection # short
title_full: Bayesian model for estimating the impact of mobility patterns on COVID-19 infection # long
date: 2020-10-23
summary: Patrick Bryant and Arne Elofsson shared code and instructions for modelling COVID-19 development using MCMC simulations based on mobile phone mobility data from Google mobility reports.
banner: /news/banners/bryant_elofsson.png
banner_large: /news/banners/bryant_elofsson_large.png
banner_caption: "Source: Part of Figure 1 of the corresponding article."
---
During the Covid-19 pandemic governments across Europe have issued non-pharmaceutical interventions (NPIs), for example social distancing and school closing, to slow down the pandemic. European countries have recommended different NPIs and the effect on mobility patterns vary between countries.

Reseachers Patrick Bryant and Arne Elofsson, using a Bayesian model, have shown that changes in mobility (using country-specific mobility data for retail and recreation, grocery and pharmacy, transit stations, workplace and residential sectors, respectively) have a considerable overlap with introduction of governmental NPIs. The results highlight the importance of government action for behavioural changes in a population. The study showed that it is hard to say what sector accounts for most of the reduction in spread, due to the high correlation of mobility in all studied sectors and epidemic spread. Still, the grocery and pharmacy sector was found to account for most of the decrease in the basic reproductive number, R0, according to the Bayesian posterior distribution.

The researchers also proposed a model that predicts 3-week epidemic forecasts by using real-time observations of changes in mobility patterns. The model may be used by both governments and regions to follow the effects NPIs have on the spread of the pandemic. The code for the MCMC simulations, written in Python using the Stan package *pystan* (v.2.19.1.1), and data from the paper are available on [GitHub](https://github.com/patrickbryant1/COVID19.github.io/tree/master/simulations/mobility)
under GPLV3 licence and supplemental information [can be found online](http://dx.doi.org/10.7717/peerj.9879).

The researchers have shared their results on the preprint server medRxiv (first version published on April 17th 2020) and gained considerable attention. Several other preprints from the researchers are also available on medRxiv (The limits of estimating COVID-19 intervention effects using Bayesian models, DOI: [10.1101/2020.08.14.20175240](https://doi.org/10.1101/2020.08.14.20175240); The effect of opening up the US on COVID-19 spread, DOI: [10.1101/2020.07.03.20145649](https://doi.org/10.1101/2020.07.03.20145649)).

*The project is part of the SciLifeLab National COVID-19 Research Program funded by Knut and Alice Wallenberg Foundation and SciLifeLab. Additionally supported by the Swedish Research Council for Natural Science, and Swedish E-science Research Center.*

#### Article

DOI: [10.7717/peerj.9879](https://doi.org/10.7717/peerj.9879)

Bryant​, P., Elofsson, A. Estimating the impact of mobility patterns on COVID-19 infection rates in 11 European countries. *Peer J* (2020) **8:e9879**
