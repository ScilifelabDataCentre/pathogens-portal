---
title: SciLifeLab Autoimmunity and Serology profiling facility SARS-CoV-2 antibody test statistics
description: SARS-CoV-2 antibody testing conducted by the SciLifeLab Auto-immunology and Serology profiling facility. This dashboard displays the total number of tests conducted, and positive and negative test results over time.
banner: /dashboard_thumbs/auto_sero.jpg
toc: false
menu:
    main:
        identifier: serology-statistics
        parent: health_data
        weight: 10
    dashboard_menu:
        identifier: serology
        name: Antibody tests for SARS-CoV-2 at SciLifeLab
aliases:
    - /data_types/health_data/serology-statistics/
dashboards_topics: [COVID-19, Infectious diseases]
---
<div class="alert alert-info">Graphs on this page are based on data as per {{% serology_date_modified %}}.</div>

#### Total serology test numbers

The total number of tests run at SciLifeLab Autoimmunity and Serology profiling facility since the start, split into tests with a positive IgG-result, tests with a negative IgG-result, and R&D tests.

<div class="d-lg-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="w-100" id="total-number"></div>
</div>

<div class="small text-muted">*The category here denoted as "R&D" (research and development) includes all remaining serum, plasma and saliva samples where we have measured the levels of IgG, IgM or IgA antibodies targeting SARS-CoV-2 proteins. It includes all positive and negative controls, all replicated and rerun of samples and assays, all samples analysed during the continuous development and optimization, technically failed samples and all research associated projects.<br> **"Proportion positive" here is the proportion of tests with a positive IgG-result out of all tests that were not R&D (i.e., the sum of tests with a positive IgG-result and tests with a negative IgG-result). </div>

#### Weekly serology test numbers

The number of tests run at SciLifeLab Autoimmunity and Serology profiling facility weekly, split into tests with a positive IgG-result, tests with a negative IgG-result, and R&D tests.

<div class="d-lg-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="w-100" id="bar-chart"></div>
</div>

<div class="small text-muted">*The category here denoted as "R&D" (research and development) includes all remaining serum, plasma and saliva samples where we have measured the levels of IgG, IgM or IgA antibodies targeting SARS-CoV-2 proteins. It includes all positive and negative controls, all replicated and rerun of samples and assays, all samples analysed during the continuous development and optimization, technically failed samples and all research associated projects.</div>

#### Cumulative serology test numbers

The sum of all tests run at SciLifeLab Autoimmunity and Serology profiling facility since the start, split into tests with a positive IgG-result, tests with a negative IgG-result, and R&D tests.

<div class="d-lg-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="w-100" id="cumulative-plot"></div>
</div>

<div class="small text-muted">*The category here denoted as "R&D" (research and development) includes all remaining serum, plasma and saliva samples where we have measured the levels of IgG, IgM or IgA antibodies targeting SARS-CoV-2 proteins. It includes all positive and negative controls, all replicated and rerun of samples and assays, all samples analysed during the continuous development and optimization, technically failed samples and all research associated projects.</div>

#### About serology testing at the Autoimmunity and Serology Profiling facility

During early phases of the Covid-19 pandemic, three [KTH](https://www.kth.se) research groups and the [Autoimmunity profiling facility](https://www.scilifelab.se/facilities/autoimmunity-profiling/) at [SciLifeLab](https://www.scilifelab.se) set out to [develop a serological assay](https://www.scilifelab.se/covid-19/kaw-program/serology/) for large scale testing of plasma and serum samples for antibodies to SARS-CoV-2. The work was initiated and coordinated by the three KTH professors Peter Nilsson, Sophia Hober and My Hedhammar.

The development of the assay has been funded by Knut and Alice Wallenberg Foundation, Erling-Persson Family Foundation, SciLifeLab, KTH, Region Stockholm, Atlas Copco, Mercodia, Family Christian and Jennifer Dahlberg, Family Birgitta Klasén.

By comparing and combining large number of variants of SARS-CoV-2 proteins as antigens, a highly sensitive and specific multiplex bead-based assay was established and applied in high throughput with up to 8000 samples analysed per week. The vast majority of samples analysed so far have been collected from health care personnel and within population based studies as well as from personnel in the pharmaceutical and biotechnology industry and also within a long range of research collaborations. Sample providers and research collaborators include [Danderyd University Hospital](https://www.scilifelab.se/news/four-out-of-five-still-have-antibodies-against-sars-cov-2), Karolinska University Hospital, Uppsala University Hospital, Skåne University Hospital, Örebro University Hospital, Sophiahemmet Hospital, Public Health Agency of Sweden, RISE Research Institutes of Sweden, AstraZeneca, Cytiva, SVPH, Karolinska Institutet, KTH, Uppsala University and Lund University.

The SciLifeLab facility has now changed its name to [Autoimmunity and Serology Profiling facility](https://www.scilifelab.se/facilities/autoimmunity-profiling/).

#### Publications and preprints

Last updated: 2021-11-15

- Peter Bergman, Ola Blennow, Lotta Hansson, Stephan Mielke, Piotr
Nowak, Puran Chen, Gunnar Söderdahl, Anders Österborg, Edvard Smith, David Wullimann, Jan Vesterbacka, Gustaf Lindgren,
Lisa Blixt, Gustav Friman, Emilie Wahren Borgstrom, Anna Nordlander, Angelica Cuapio Gomez, Mira Akber, Davide Valentini,
Anna-Carin Norlin, Anders Thalme, Gordana Bogdanovic, Sandra Muschiol, Peter Nilsson, Sophia Hober, Karin Lore, Margaret
Sällberg Chen, Marcus Buggert, Hans-Gustav Ljunggren, Per Ljungman, Soo Aleman. Safety and efficacy of the mRNA BNT162b2 vaccine against SARS-CoV-2 in five groups of immunocompromised patients and
healthy controls in a prospective open-label clinical trial. *EBioMedicine* **in press**. [https://doi.org/10.1101/2021.09.07.21263206](https://doi.org/10.1101/2021.09.07.21263206)

- Raphael Carapito, Richard Li, Julie Helms, Christine Carapito, Sharvari Gujja, Véronique Rolli, Raony Guimaraes, Jose Malagon-
Lopez, Perrine Spinnhirny, Razieh Mohseninia, Aurélie Hirschler, Leslie Muller, Paul Bastard, Adrian Gervais, Qian Zhang,
Francois Danion, Yvon Ruch, Maleka Schenck-Dhif, Olivier Collange, Thiên-Nga Chamaraux-Tran, Anne Molitor, Angélique
Pichot, Alice Bernard, Ouria Tahar, Sabrina Bibi-Triki, Haiguo Wu, Nicodème Paul, Sylvain Mayeur, Annabel Larnicol, Geraldine
Laumond, Julia Frappier, Sylvie Schmidt, Antoine Hanauer, Cécile Macquin, Tristan Stemmelen, Michael Simons, Xavier
Mariette, Olivier Hermine, Samira Fafi-Kremer, Bernard Goichot, Bernard Drenou, Khaldoun Kuteifan, Julien Pottecher, Paul-
Michel Mertes, Shweta Kailasan, M. Javad Aman, Elisa Pin, Peter Nilsson, Anne Thomas, Alain Viari, Damien Sanlaville, Francis
Schneider, Jean Sibilia, Pierre-Louis Tharaux, Jean-Laurent Casanova, Yves Hansmann, Daniel Lidar, Mirjana Radosavljevic,
Jeffrey Gulcher, Ferhat Meziani, Christiane Moog, Thomas W Chittenden, Seiamak Bahram. Identification of driver genes for severe forms of COVID-19 in a deeply phenotyped young patient cohort. *Science Translational Medicine* (2021). [https://doi.org/10.1126/scitranslmed.abj7521](https://doi.org/10.1126/scitranslmed.abj7521)

- Sara Mravinacova, Malin Jönsson, Jonas Klingström, Jamil Yousef, Cecilia Hellström, Sebastian Havervall, Sara Kanje, Charlotte Thålin, Elisa Pin, Hanna Tegel, Peter
Nilsson, Anna Månberg, Sophia Hober. A cell free high-throughput assay for assessment of SARS-CoV-2 neutralization capability. *New Biotechnology* **66** (2022). [https://doi.org/10.1016/j.nbt.2021.10.002](https://doi.org/10.1016/j.nbt.2021.10.002)

- Sebastian Havervall, Ulrika Marking, Nina Greilert-Norin, Max Gordon, Henry Ng, Wanda Christ, Kim Blom, Mia Phillipson, Peter Nilsson, Sophia Hober, Jonas Klingström,
Sara Mangsbo, Mikael Åberg, Charlotte Thålin. Impact of SARS-CoV-2 infection on vaccine-induced immune responses over time. *medRxiv* (2021). [https://doi.org/10.1101/2021.10.16.21264948](https://doi.org/10.1101/2021.10.16.21264948)

- Katie Healy, Elisa Pin, Puran Chen, Gunnar Söderdahl, Piotr Nowak, Stephan Mielke, Lotta Hansson, Peter Bergman,
Edvard Smith, Per Ljungman, Davide Valentini, Ola Blennow, Anders Österborg, Giorgio Gabarrini, Khaled Al-Manei, Hassan
Alkharaan, Michal Jacek Sobkowiak, Xinling Xu, Mira Akber, Karin Loré, Cecilia Hellström, Sandra Muschiol, Gordana
Bogdanovic, Markus Buggert, Hans-Gustaf Ljunggren, Sophia Hober, Peter Nilsson, Soo Aleman, Margaret Sällberg Chen. Appearance of IgG to SARS-CoV-2 in saliva effectively indicates seroconversion in mRNA vaccinated immunocompromised
individuals. *medRxiv* (2021). [https://doi.org/10.1101/2021.09.30.21264377](https://doi.org/10.1101/2021.09.30.21264377)

- Sara M Mangsbo, Sebastian Havervall, Ida Laurén, Robin Lindsay, August Jernbom Falk, Ulrika Marking, Martin Lord, Marcus Buggert, Pierre
Dönnes, Gustaf Christoffersson, Peter Nilsson, Sophia Hober, Mia Phillipson, Jonas Klingström, Charlotte Thålin. An evaluation of a FluoroSpot assay as a diagnostic tool to determine SARS-CoV-2 specific T-cell responses. *PLOS ONE* **16(9)** (2021). [https://doi.org/10.1371/journal.pone.0258041](https://doi.org/10.1371/journal.pone.0258041)

- Lisa Blixt, Gordana Bogdanovic, Marcus Buggert, Yu Gao, Sophia Hober, Katie Healy, Hemming
Johansson, Christian Kjellander, Sara Mravinacova, Sandra Muschiol, Peter Nilsson, Marzia Palma, Elisa Pin, C.I. Edvard Smith,
Olga Stromberg, Margaret Sällberg Chen, Rula Zain, Lotta Hansson and Anders Österborg. Covid-19 in patients with chronic lymphocytic leukemia: Clinical outcome and B- and T-cell immunity during 13 months in
consecutive patients. *Leukemia* (2021). [https://doi.org/10.1038/s41375-021-01424-w](https://doi.org/10.1038/s41375-021-01424-w)

- Klara Asplund Högelin; Nicolas Ruffin; Elisa Pin; Anna Månberg; Sophia Hober; Guro Gafvelin; Hans Grönlund;
Peter Nilsson; Mohsen Khademi; Tomas Olsson; Fredrik Piehl; Faiez Al Nimer. Development of humoral and cellular immunological memory against SARS-CoV-2 despite B-cell depleting treatment in
multiple sclerosis. *iScience* **24(9)**. [https://doi.org/10.1016/j.isci.2021.103078](https://doi.org/10.1016/j.isci.2021.103078)

- Sebastian Havervall, Henry Ng, August Jernbom Falk, Nina Greilert-Norin, Anna Månberg, Ulrika
Wimmercranz-Marking, Ida Laurén, Lena Gabrielsson, Ann-Christin Salomonsson, Katherina Aguilera, Martha Kihlgren, Maja
Månsson, Cecilia Hellström, Eni Andersson, Jennie Olofsson, Lovisa Skoglund, Jamil Yousef, Elisa Pin, Martin Lord, My
Hedhammar, Hanna Tegel, Pierre Dönnes, Mia Phillipson, Peter Nilsson, Jonas Klingström, Sara Mangsbo, Sophia Hober,
Charlotte Thålin. Robust humoral and cellular immune responses and low risk for reinfection at least eight months following asymptomatic
to mild COVID-19. *J Internal Medicine* (2021). [https://doi.org/10.1111/joim.13387](https://doi.org/10.1111/joim.13387)

- Miriam Elfström, Jonas Blomqvist, Peter Nilsson, Sophia Hober, Elisa Pin, Anna Månberg, Ville N. Pimenoff, Laila Sara Arroyo Mühr, Kalle Conneryd Lundgren, Joakim Dillner. Differences in risk for SARS-CoV-2 infection among healthcare workers. *Preventive Medicine Reports* **24** (2021). [https://doi.org/10.1016/j.pmedr.2021.101518](https://doi.org/10.1016/j.pmedr.2021.101518)

- Sebastian Havervall, Ulrika Marking, Nina Greilert-Norin, Henry Ng, Ann-Christin Salomonsson, Cecilia Hellström, Elisa
Pin, Kim Blom, Sara Mangsbo, Mia Phillipson, Jonas Klingström, Mikael Åberg, Sophia Hober, Peter Nilsson, Charlotte Thålin. Antibody Responses After a Single Dose of ChAdOx1 nCoV-19 Vaccine in Healthcare Workers Previously Infected with SARS-
CoV-2. *EBioMedicine* **70** (2021). [https://doi.org/10.1016/j.ebiom.2021.103523](https://doi.org/10.1016/j.ebiom.2021.103523)

- Sebastian Havervall, Ulrika Marking, Max Gordon, Henry Ng, Nina Greilert-Norin, Sarah Lindbo, Kim Blom, Peter Nilsson, Mia Phillipson, Jonas Klingström, Sara Mangsbo, Mikael
Åberg, Sophia Hober, Charlotte Thålin. Neutralization of VOCs including Delta one year post COVID-19 or vaccine. *medRxiv* (2021). [https://doi.org/10.1101/2021.08.12.21261951](https://doi.org/10.1101/2021.08.12.21261951)

- Sophia Hober, Cecilia Hellström, Jennie Olofsson, Eni Andersson, Sofia Bergström, August Jernbom Falk, Shaghayegh Bayati,
Sara Mravinacova, Ronald Sjöberg, Jamil Yousef, Lovisa Skoglund, Sara Kanje, Anna Berling, Anne-Sophie Svensson, Gabriella
Jenssen, Henric Enstedt, Delaram Afshari, Lan Xu, Martin Zwahlen, Kalle von Feilitzen, Leo Hanke, Ben Murrell, Gerald
McInerney, Gunilla B. Karlsson Hedestam, Christofer Lendel, Robert G. Roth, Ingmar Skoog, Elisabet Svenungsson, Tomas
Olsson, Anna Fogdell-Hahn, Ylva Lindroth, Maria Lundgren, Kimia T. Maleki, Nina Lagerqvist, Jonas Klingström, Rui Da Silva
Rodrigues, Sandra Muschiol, Gordana Bogdanovic, Laila Sara Arroyo Mühr, Carina Eklund, Camilla Lagheden, Joakim Dillner,
Åsa Sivertsson, Sebastian Havervall, Charlotte Thålin, Hanna Tegel, Elisa Pin, Anna Månberg, My Hedhammar, Peter Nilsson. Systematic evaluation of SARS-CoV-2 antigens enables a highly specific and sensitive multiplex serological COVID-19 assay. *Clinical & Translational Immunology* **e1312** (2021). [http://dx.doi.org/10.1002/cti2.1312](http://dx.doi.org/10.1002/cti2.1312)

- Susanna Klevebro, Fuad Bahram, Miriam Elfström, Ulrika Hellberg, Sophia Hober, Simon Kebede Merid, Inger Kull, Peter Nilsson, Per
Tornvall, Gang Wang, Kalle Conneryd Lundgren, Sari Ponzer, Joakim Dillner, Erik Melén. Risk of SARS-CoV-2 exposure among hospital healthcare workers in relation to patient contact and type of care. *Scand J Publ Health* **49** (2021). [https://journals.sagepub.com/doi/10.1177/14034948211022434](https://journals.sagepub.com/doi/10.1177/14034948211022434)

- Thomas Åkerlund, Katherina Zakikhany, Charlotta Löfström, Evelina Lindmark, Henrik Källberg, Ulla Elofsson, Karin Cederbrant, Erik Nygren, Anders Kallin, Nina Lagerkvist, Peter
Nilsson, Sophia Hober, Anna Ridderstad Wollberg, Åsa Szekely Björndal. Stable IgG-antibody levels in patients with mild SARS-CoV-2 infection. *medRxiv* (2021). [https://doi.org/10.1101/2021.06.16.21258960](https://doi.org/10.1101/2021.06.16.21258960)

- Hassan Alkharaan, Shaghayegh Bayati, Cecilia Hellström, Annika Olsson, Karin Lindahl, Gordana Bogdanovic, Soo Aleman, Georgios Tsilingaridis, Patricia De Palma, Sophia Hober, Anna Månberg, Peter Nilsson, Elisa Pin, Margaret Sällberg
Chen. Persisting Salivary IgG against SARS-CoV-2 at 9 Months After Mild COVID-19 – A Complementary Approach to Population
Surveys. *J Infectious Diseases* **224** (2021). [https://doi.org/10.1093/infdis/jiab256](https://doi.org/10.1093/infdis/jiab256)

- Nastya Kharlamova, Nicky Dunn, Sahl Khalid Bedri, Svante Jerling, Malin Almgren, Francesca Faustini, Iva Gunnarsson, Johan Rönnelid,
Rille Pullerits, Inger Gjertsson, Karin Lundberg, Anna Månberg, Elisa Pin, Peter Nilsson, Sophia Hober, Katharina Fink and Anna
Fogdell-Hahn. False positive results in SARS-CoV-2 serological tests for samples from patients with chronic inflammatory diseases. *Frontiers in Immunology* **12** (2021). [https://doi.org/10.3389/fimmu.2021.666114](https://doi.org/10.3389/fimmu.2021.666114)

- Sebastian Havervall, Axel Rosell, Mia Phillipson, Sara Mangsbo, Peter Nilsson, Sophia Hober, Charlotte Thålin. Symptoms and functional impairment assessed 8 months after mild COVID-19 among health care workers. *JAMA* **325** (2021).

- Sadaf Sakina Hassan, Åsa Seigerud, Roda Abdirahman, Laila Sara Arroyo Mühr, Sara Nordqvist-Kleppe, Elisa Pin, Anna Månberg, Sophia
Hober, Peter Nilsson, Lars Engstrand, Miriam Elfström, Jonas Blomqvist, Kalle Conneryd-Lundgren, Joakim Dillner. SARS-CoV-2 infections among personnel providing home care services for older persons in Stockholm, Sweden. *J Internal Medicine* **290** (2021). [https://doi.org/10.1111/joim.13274](https://doi.org/10.1111/joim.13274)

- Joakim Dillner, Miriam Elfström, Jonas Blomqvist, Carina Eklund, Camilla Lagheden, Sara Nordqvist-Kleppe, Cecilia Hellström, Jennie Olofsson, Eni Andersson, August Jernbom Falk, Sofia
Bergström, Emilie Hultin, Elisa Pin, Anna Månberg, Peter Nilsson, My Hedhammar, Sophia Hober, Johan Mattsson, Laila Sara
Arroyo Mühr, Kalle Conneryd Lundgren. Antibodies to SARS-CoV-2 and risk of past or future sick leave. *Scientific Reports* **11** (2021). [https://doi.org/10.1038/s41598-021-84356-w](https://doi.org/10.1038/s41598-021-84356-w)

- Joakim Dillner, Miriam Elfström, Jonas Blomqvist, Lars Engstrand, Mathias Uhlén, Carina Eklund, Fredrik Boulund, Camilla Lagheden, Marica Hamsten, Sara
Nordqvist-Kleppe, Maike Seifert, Cecilia Hellström, Jennie Olofsson, Eni Andersson, August Jernbom Falk, Sofia Bergström,
Emilie Hultin, Elisa Pin, Ville N Pimenoff, Sadaf Hassan, Anna Månberg, Peter Nilsson, My Hedhammar, Sophia Hober, Johan
Mattsson, Laila Sara Arroyo Mühr, Kalle Conneryd-Lundgren. High amounts of SARS-CoV-2 precede sickness among asymptomatic healthcare workers. *J Infectious Diseases* **224** (2021). [https://doi.org/10.1093/infdis/jiab099](https://doi.org/10.1093/infdis/jiab099)

- Sebastian Havervall, August Jernbom Falk, Jonas Klingström, Henry Ng, Nina Greilert-Norin, Lena Gabrielsson, Ann-Christin
Salomonsson, Eva Isaksson, Ann-Sofie Rudberg, Cecilia Hellström, Eni Andersson, Jennie Olofsson, Lovisa Skoglund, Jamil
Yousef, Elisa Pin, Wanda Christ, Mikaela Olausson, My Hedhammar, Hanna Tegel, Sara Mangsbo, Mia Phillipson, Anna
Månberg, Sophia Hober, Peter Nilsson, Charlotte Thålin. SARS-CoV-2 induces a durable and antigen specific humoral immunity after asymptomatic to mild COVID-19 infection. *medRxiv* (2021) [https://doi.org/10.1101/2021.01.03.21249162](https://doi.org/10.1101/2021.01.03.21249162)

- Ann-Sofie Rudberg, Sebastian Havervall, Anna Månberg, August Jernbom Falk, Katherina Aguilera, Henry Ng, Lena Gabrielsson, Ann-Christin Salomonsson,
Leo Hanke, Ben Murrell, Gerald McInerney, Jennie Olofsson, Eni Andersson, Cecilia Hellström, Shaghayegh Bayati, Sofia
Bergström, Elisa Pin, Ronald Sjöberg, Hanna Tegel, My Hedhammar, Mia Phillipson, Peter Nilsson, Sophia Hober, Charlotte
Thålin. SARS-CoV-2 exposure, symptoms and seroprevalence in healthcare workers in Sweden. *Nature Communications* **11** (2020). [https://doi.org/10.1038/s41467-020-18848-0](https://doi.org/10.1038/s41467-020-18848-0)

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.12.2"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dc.scilifelab.se/graphic/e5c031600d334d889f33080d3f0ac0dd.js?id=bar-chart"></script>
<script src="https://datagraphics.dc.scilifelab.se/graphic/4c635b2679e648e384d952dd3e506ff1.js?id=cumulative-plot"></script>
<script src="https://datagraphics.dc.scilifelab.se/graphic/63d9201aee8747c9b37c17ebb6b01c35.js?id=total-number"></script>
