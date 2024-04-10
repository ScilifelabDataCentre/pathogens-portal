"""
    This file contains JSON template used in the script update_index_json.py
"""

json_templete = '''
{{
  "name": "Swedish Pathogens Portal",
  "release": "{release}",
  "release_date": "{release_date}",
  "entry_count": 18,
  "entries": [
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset1"
        }},
        {{
          "name": "name",
          "value": "Antibody testing for SARS-CoV-2 at SciLifeLab, Sweden"
        }},
        {{
          "name": "description",
          "value": "SARS-CoV-2 antibody testing conducted by the SciLifeLab Auto-immunology and Serology profiling facility. This dashboard displays the total number of tests conducted, and positive and negative test results over time"
        }},
        {{
          "name": "updated_date",
          "value": "23-07-11"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Serology"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "Early in the COVID-19 pandemic, work was initiated to develop a serological assay for large scale testing of plasma and serum samples for antibodies against SARS-CoV-2. The work was undertaken by three research groups at KTH Royal Institute of Technology (KTH) and the Autoimmunity and Serology Profiling unit at SciLifeLab. The development of the assay has been funded by Knut and Alice Wallenberg Foundation, Erling-Persson Family Foundation, SciLifeLab, KTH, Region Stockholm, Atlas Copco, Mercodia, Family Christian and Jennifer Dahlberg, and Family Birgitta Klasén. By comparing and combining a large number of variants of SARS-CoV-2 proteins as antigens, a highly sensitive and specific multiplex bead-based assay was established. The high-throughput assay can be used to process up to 8000 samples per week. The vast majority of samples analysed to date originated from healthcare personnel, population-based studies, personnel in the pharmaceutical and biotechnology industry, and from within multiple research collaborations. Collaborators and sample providers include Danderyd University Hospital (see news involving a follow-up study at Danderyd University Hospital), Karolinska University Hospital, Uppsala University Hospital, Skåne University Hospital, Örebro University Hospital, Sophiahemmet Hospital, Public Health Agency of Sweden, RISE (Research Institutes of Sweden), AstraZeneca, Cytiva, SVPH, Karolinska Institutet, KTH, Uppsala University, and Lund University."
        }},
        {{
          "name": "data_source",
          "value": "Autoimmunity and Serology profiling facility"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/serology-statistics/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset2"
        }},
        {{
          "name": "name",
          "value": "Data from COVID Symptom Study Sweden"
        }},
        {{
          "name": "description",
          "value": "The COVID Symptom Study Sweden (CSSS) collects data on COVID-19 prevalence, symptoms, and vaccinations through a smart phone app with over 200.000 users in Sweden. Raw data can be requested for use in research projects."
        }},
        {{
          "name": "updated_date",
          "value": "22-07-12"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Case_number"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "COVID Symptom Study Sweden uses a non-commercial app for data collection from volunteer study participants. Anyone 18 years or older living in Sweden can participate in the study."
        }},
        {{
          "name": "data_source",
          "value": "Lund University and Uppsala University"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/symptom_study_sweden/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset3"
        }},
        {{
          "name": "name",
          "value": "Swedish COVID-19 publication database"
        }},
        {{
          "name": "description",
          "value": "A summary of the COVID-19 and SARS-CoV-2 publications produced involving at least one contributor affiliated with a Swedish university or research institute. Shows publications over time and key words/phrases within them."
        }},
        {{
          "name": "updated_date",
          "value": "24-03-05"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Publications"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "This section presents a list of published scientific journal articles and preprints on COVID-19 and SARS-CoV-2 where at least one author has an affiliation with a Swedish research institute. Note that this database is primarily a manually curated database and thus it may not be exhaustive. Note that from May 2023, we began to use the Europe PMC REST API to idenfy publications. The scripts that we use to do this are openly available on GitHub and can be reused with other pathogens."
        }},
        {{
          "name": "data_source",
          "value": "Europe PMC"
        }},
        {{
          "name": "source_page",
          "value": "https://pathogens.se/publications/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset4"
        }},
        {{
          "name": "name",
          "value": "Data from the CRUSH Covid Uppsala study"
        }},
        {{
          "name": "description",
          "value": "CRUSH Covid maps outbreaks in Uppsala County by visualising the number of cases, test positivity, and geographic distribution, among other things. Data for each postal code is available for download and reuse."
        }},
        {{
          "name": "updated_date",
          "value": "22-09-15"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Case_number"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "Data from across the county of Uppsala was collected by the CRUSH Covid team. In particular, data was collected on the population size, adult population size, case numbers, and amount of testing were collected for each postcode in each week."
        }},
        {{
          "name": "data_source",
          "value": "Region Uppsala and Uppsala University, plus supporting partners"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/crush_covid/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset5"
        }},
        {{
          "name": "name",
          "value": "COVID-19 test statistics from the National Pandemic Centre"
        }},
        {{
          "name": "description",
          "value": "The National Pandemic Centre (NPC) conducted testing related to SARS-CoV-2 from the start of the pandemic. They show positive, negative, and inconclusive tests. This dashboard is historic, so no longer updated."
        }},
        {{
          "name": "updated_date",
          "value": "20-12-21"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "PCR_testing"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "The National Pandemic Centre (NPC) was a facility for SARS-CoV-2 (COVID-19) testing established within the Centre for Translational Microbiome Research (CTMR) at Karolinska Institutet (KI)/SciLifeLab. At the end of March 2020, the large-scale microbiome research lab was quickly converted into a centre to assist Sweden with analysing SARS-CoV-2 tests. This was made possible by a donation from the Knut and Alice Wallenberg Foundation (KAW) and a previously established collaboration with MGI Tech in Shenzen, China. The NPC initially helped to expand the RNA-extraction capacity at Karolinska Universitets laboratoriet. However, it quickly expanded into a facility that increased the testing capacity across all regions of Sweden. The final capacity of the National Pandemic Centre at KI/SciLifeLab was approximately 10,000 tests per day. The results were typically returned within 24 hours of the sample arriving to the lab. NPC exclusively performed PCR-based analyses, not serological (antibody-based) analyses."
        }},
        {{
          "name": "data_source",
          "value": "Karolinska Institutet"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/npc-statistics/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset6"
        }},
        {{
          "name": "name",
          "value": "Data on the occurrence of post COVID-19 condition (long COVID) in Sweden"
        }},
        {{
          "name": "description",
          "value": "The Swedish Board of Health and Welfare (Socialstyrelsen) collects data on the occurence of post COVID-19 condition (long COVID) across Sweden. Here, we show visualisations of data on symptoms, healthcare contacts, and geographic distribution of cases, among other things."
        }},
        {{
          "name": "updated_date",
          "value": "24-02-16"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Postcovid_occurrence"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "The Swedish Board of Health and Welfare (Socialstyrelsen) has been collecting data on the amount of cases of post COVID-19 condition (otherwise known as long-covid) in Sweden. This includes the occurence of multiple diagnosis codes (U09.9 and Z86.1A/U80.9). It also includes information related to contacts with healthcare."
        }},
        {{
          "name": "data_source",
          "value": "The Swedish Board of Health and Welfare (Socialstyrelsen)"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/post_covid/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset7"
        }},
        {{
          "name": "name",
          "value": "Data from register-based large-scale national population study to monitor COVID-19 vaccination effectiveness and safety (RECOVAC)"
        }},
        {{
          "name": "description",
          "value": "Data from the register-based large-scale national population study to monitor COVID-19 vaccination effectiveness and safety (RECOVAC) project. The project includes data on vaccination coverage, comorbidities, and admissions to intensive care units."
        }},
        {{
          "name": "updated_date",
          "value": "{dataset7_modified}"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Registry"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "The data in this study are pseudonymised individual-level data from Swedish healthcare registers and have been compiled for the scientific purposes of the RECOVAC and SCIFI-PEARL project, as they are available from the respective Swedish public data holders on the basis of ethics approval for the research in question, subject to relevant legislation, processes and data protection."
        }},
        {{
          "name": "data_source",
          "value": "RECOVAC study"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/recovac/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset8"
        }},
        {{
          "name": "name",
          "value": "SARS-CoV-2 whole genome sequencing"
        }},
        {{
          "name": "description",
          "value": "Surveillance of viral genome sequences is crucial in tracking the spread of viral variants. This dashboard shows whole-genome sequencing data generated by Uppsala University Hospital."
        }},
        {{
          "name": "updated_date",
          "value": "{dataset8_modified}"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Variant_classifications"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "Throughout the pandemic and until present day, the section for Clinical Microbiology and Hospital Hygiene at Uppsala University Hospital have conducted surveillance for SARS-CoV-2 in Uppsala. To do this, they performed whole genome sequencing on samples from SARS-CoV-2 positive patients in the Uppsala region. Throughout the COVID-19 pandemic, they sequenced over 12,000 samples from Uppsala."
        }},
        {{
          "name": "data_source",
          "value": "Uppsala University Hospital and Uppsala University"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/variants_region_uppsala/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset9"
        }},
        {{
          "name": "name",
          "value": "Vaccine administration: COVID-19"
        }},
        {{
          "name": "description",
          "value": "The Swedish Health Agency (Folkhälsomyndigheten) provides data and information related to COVID-19 in Sweden. Visualisations are shown on multiple aspects of vaccination coverage, like coverage in different counties."
        }},
        {{
          "name": "updated_date",
          "value": "22-10-01"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Vaccination"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "The Swedish Health agency compiled information about the coverage of vaccinations in Sweden. This included information on the coverage of each dose up to 5 doses. It also contained information about vaccine coverage according to geographic dustribution and age group."
        }},
        {{
          "name": "data_source",
          "value": "Swedish Health Agency (Folkhälsomyndigheten)"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/vaccines/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset10"
        }},
        {{
          "name": "name",
          "value": "SARS-CoV-2 quantification in wastewater (Gothenburg University)"
        }},
        {{
          "name": "description",
          "value": "Quantification of the levels of SARS-CoV-2 in wastewater from Gothenburg by the Norder group at Gothenburg University (GU)"
        }},
        {{
          "name": "updated_date",
          "value": "{dataset10_modified}"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Wastewater"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "Samples of wastewater were collected using a fixed-site sampler that collected 30ml per 10,000m3 of the incoming wastewater. For the purposes of analysis, seven samples (each representing a 24 hour period) were pooled to create a weekly sample. The weekly sample, which consisted of 1.5-15l of wastewater (depending on the flow) was sent to the Clinical Microbiology Laboratory at Sahlgrenska University Hospital for analysis. Analyses were conducted on the Monday after the sample was collected. At the Clinical Microbiology Laboratory, two methods developed in-house were used to concentrate viruses. The current method uses ultrafiltration as the primary method of concentration. Our previous method instead used an electropositive filter (Saguti et al., 2021). The two techniques were used in parallel between weeks 20 and 43 in 2023. All information related to the data collected using the previous method can be found on the page related to historic SARS-CoV-2 data from Gothenburg. Nucleic acids were extracted from 1ml of the concentrated sample using the QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Real-time quantitative PCR (RT-qPCR) was performed to detect the RNA-dependent RNA polymerase (RdRP) region of SARS-CoV-2. In all runs, a 10-fold serial diluted plasmid (Eurofins Genomics, Ebersberg, Germany) that contained the target SARS-CoV-2 region was used as a positive control. Nuclease-free water was used as a negative control. Details about the method of calculation are provided in Hellmér et al. (2014), Saguti et al. (2021), Wang et al. (2022), and Wang et al. (2023)."
        }},
        {{
          "name": "data_source",
          "value": "Gothenburg University"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/wastewater/covid_quantification/covid_quant_gu/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset11"
        }},
        {{
          "name": "name",
          "value": "Historic data for SARS-CoV-2 quantification in wastewater (Gothenburg University)"
        }},
        {{
          "name": "description",
          "value": "This data was collected between week 7 of 2020, and week 43 of 2023 (i.e. between 10th February 2020 and 23rd October 2023). A different method was used compared to contemporarily updated data."
        }},
        {{
          "name": "updated_date",
          "value": "23-10-23"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Wastewater"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "Samples of wastewater were collected using a fixed-site sampler that collected 30ml per 10,000m3 of the incoming wastewater. For the purposes of analysis, seven samples (each representing a 24 hour period) were pooled to create a weekly sample. The weekly sample, which consisted of 1.5-15l of wastewater (depending on the flow) was sent to the Clinical Microbiology Laboratory at Sahlgrenska University Hospital for analysis. Analyses were conducted on the Monday after the sample was collected. At the Clinical Microbiology Laboratory, viruses were concentrated to a final volume of 2.5ml, using a method that was developed in-house. This method uses the NanoCeram electropositive filter (Argonide, Florida, USA) as the primary means of concentration, and then ultracentrifugation as secondary concentration method (Saguti et al., 2021). Nucleic acids were extracted from 1ml of the concentrated sample using the QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Real-time quantitative PCR (RT-qPCR) was performed to detect the RNA-dependent RNA polymerase (RdRP) region of SARS-CoV-2. In all runs, a 10-fold serial diluted plasmid (Eurofins Genomics, Ebersberg, Germany) that contained the target SARS-CoV-2 region was used as a positive control. Nuclease-free water was used as a negative control. The Ct values from the qPCR were used to quantify the amount of SARS-CoV-2 genome in the sample. Details about the method of calculation are provided in Saguti et al. (2021). The relative amount of viral genome in the wastewater was calculated by dividing the amount of viral genome in the sample by the amount of SARS-CoV-2 genome in the incoming wastewater during week 11 (mid-March) of 2020. Samples from all subsequent weeks contained detectable SARS-CoV-2 genome."
        }},
        {{
          "name": "data_source",
          "value": "Gothenburg University"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/wastewater/covid_quantification/historic_covid_gu/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset12"
        }},
        {{
          "name": "name",
          "value": "SARS-CoV-2 quantification in wastewater (SEEC-KTH)"
        }},
        {{
          "name": "description",
          "value": "Quantification of the levels of SARS-CoV-2 in wastewater from Stockholm and Malmö by the SEEC-KTH node (no longer updated after June 2023, historic data is available)."
        }},
        {{
          "name": "updated_date",
          "value": "23-06-02"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Wastewater"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "To correct for variations in population size and wastewater flow, the group quantifies the pepper mild mottle virus (PMMoV) using a modified version of the assay of Zhang et al. (2006). PMMoV is an abundant RNA virus in human faeces and serves as an estimator of human faecal content (Symonds et al., 2019). SARS-like virus specific N3-primers (Lu et al., 2020) with SYBR Green chemistry (Perez-Zabaleta et al., 2023) are used to quantify SARS-CoV-2. After concentration, filtering, and preparation, the samples are analysed using the qPCR technique for SARS CoV-2 RNA. Primers of the nucleocapsid (N) gene were used to detect the SARS-COV-2 gene (previously used and verified by Medema et al. (2020)). In some cases, raw wastewater samples were frozen at -20℃, and concentrated wastewater or purified RNA samples were sometimes stored at -80℃ before the next analysis step was carried out. The concentration method initially used by SEEC-KTH was based on one of their earlier studies (Jafferali et al., 2021), which compared four different concentration methods. This method was used until week 35 of 2021. After this time, the group began to instead use the Promega kit for the concentration step."
        }},
        {{
          "name": "data_source",
          "value": "KTH Royal Institute of Technology"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/wastewater/covid_quantification/covid_quant_kth/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset13"
        }},
        {{
          "name": "name",
          "value": "Historic data for SARS-CoV-2 quantification in wastewater from Stockholm (SEEC-KTH)"
        }},
        {{
          "name": "description",
          "value": "This data shows the amount of SARS-CoV-2 in wastewater from Stockholm between April 2020 and August 2021, calculated as gene copy number/week (raw wastewater) with bovine + PMMoV factor. The method used has since been updated by the research group for more recent data."
        }},
        {{
          "name": "updated_date",
          "value": "21-08-31"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Wastewater"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "After concentration, filtering, and preparation, the samples are analyzed using qPCR technique for SARS CoV-2 RNA. Primers of the nucleocapsid (N) gene were used to detect the SARS-COV-2 gene (previously used and verified by Medema and colleagues (2020)). In some cases, the raw wastewater has been frozen at –20 degrees, and concentrated wastewater or purified RNA have been stored at -80 C before the next analysis step was carried out. The concentration method used by prof. Zeynep Cetecioglu Gurol and her colleagues are based on their published study (Jafferali and colleagues, 2021) comparing four different concentration methods. The study concluded that the double ultrafiltration method adapted by KTH has a significantly higher efficiency compared to single filtration and adsorption methods."
        }},
        {{
          "name": "data_source",
          "value": "KTH Royal Institute of Technology"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/wastewater/covid_quantification/historic_stockholm/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset14"
        }},
        {{
          "name": "name",
          "value": "SARS-CoV-2 quantification in wastewater (SEEC-SLU)"
        }},
        {{
          "name": "description",
          "value": "Quantification of the levels of SARS-CoV-2 in wastewater from multiple sites, including Stockholm, Malmö, Gothenburg, Uppsala, Västerås, Örebro, Umeå, and many others, by the SEEC-SLU node"
        }},
        {{
          "name": "updated_date",
          "value": "{dataset14_modified}"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Wasterwater"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "For most cities represented, raw, untreated wastewater samples that are representative of a single day are collected by flow compensated samplers at the wastewater treatment plants (WWTP). Uppsala is the exception, with all measurements since week 16 of 2021 instead representing 1 week. In Uppsala, samples are collected daily, and then combined flow-proportionally into one composite weekly sample for the purpose of analyses. The freshly collected samples are processed according to standard methodologies. For samples collected up to and including week 18 of 2021, viral particles were concentrated using the electronegative filtration method (Ahmed et al., 2020). Since week 19 of 2021, the viral genomic material has instead been concentrated and extracted by the direct capture method, using the Maxwell RSC Enviro TNA kit (Promega). Absolute quantification of the copy numbers of the SARS-CoV-2 genome is performed using One-Step RT-qPCR. Until week 31 of 2023 the quantification of the viral genomes was performed using the SARS-CoV-2 specific N1 assay from the Centers for Disease Control and Prevention (CDC). From week 32 of 2023 quantification is performed using the Flu SC2 Multiplex Assay (CDC). To correct for variations in population size and wastewater flow, the pepper mild mottle virus (PMMoV) is quantified using a modified version of the assay of Zhang et al. (2006). PMMoV is an abundant RNA virus in human faeces and serves as an estimator of human faecal content (Symonds et al., 2019). For more details about the sample processing method, and the evaluation of the use of the PMMoV normalisation method for Swedish wastewater, please refer to the corresponding publication: Isaksson et al. (2022). The data in the graph and datafile represent the ratio of the copy numbers measured by the Flu SC2 Multiplex Assay and PMMoV-assays, multiplied by 1000. As the Flu SC2 Multiplex Assay provides a proxy for SARS-CoV-2 virus content in the wastewater and PMMoV is a proxy of the faecal content (which is related to the contributing population), the ratio of the two can be considered to be a proxy for the prevalence of COVID-19 infections in the population of the wastewater catchment area. To align the data generated by the current method with the data generated by methods and quantification assays used earlier, older data has been transformed using conversion factors. The conversion factors are estimated based on common alignment periods when old and new methods are used in parallel."
        }},
        {{
          "name": "data_source",
          "value": "Swedish University of Agricultural Sciences (SLU)"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/wastewater/covid_quantification/covid_quant_slu/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset15"
        }},
        {{
          "name": "name",
          "value": "Historic data for SARS-CoV-2 quantification in wastewater from Örebro and Umeå(SEEC-SLU)"
        }},
        {{
          "name": "description",
          "value": "This data shows the amount of SARS-CoV-2 in Umeå and Örebro wastewater between October 2020 and June 2021. The methodology used has since been updated by the group for more recent data."
        }},
        {{
          "name": "updated_date",
          "value": "21-06-30"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Wastewater"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "SARS-CoV-2"
        }},
        {{
          "name": "methods",
          "value": "After preparation, the viruses were extracted using ultra filtration and analyzed using qPCR technique for SARS CoV-2 RNA. Primers were used to detect the SARS-COV-2 gene (previously used and verified by Corman and colleagues (2020)). qPCR samples were normalized against PMMV."
        }},
        {{
          "name": "data_source",
          "value": "Swedish University of Agricultural Sciences (SLU)"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/wastewater/covid_quantification/historic_orebro_umea/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset16"
        }},
        {{
          "name": "name",
          "value": "Enteric virus quantification in wastewater (Gothenburg University)"
        }},
        {{
          "name": "description",
          "value": "Quantification of the levels of multiple enteric viruses (enterovirus, adenovirus, GG2, astrovirus, sapovirus) and PPMoV (as a control) in wastewater from Gothenburg by the Norder group at Gothenburg University (GU)"
        }},
        {{
          "name": "updated_date",
          "value": "{dataset16_modified}"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Wastewater"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "Enterovirus"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "Adenovirus"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "GG2"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "Astrovirus"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "Sapovirus"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "PMMoV"
        }},
        {{
          "name": "methods",
          "value": "Samples of wastewater are collected using a fixed-site sampler that collects 30ml per 10,000m3 of the incoming wastewater. For the purposes of analysis, seven samples (each representing a 24 hour period) were pooled to create a weekly sample. Part of this weekly sample was sent to the Clinical Microbiology Laboratory at Sahlgrenska University Hospital for analysis. The amount of sample sent varies between 1.5-15l of wastewater, depending on the flow. Whilst the amount of wastewater from households and industry is generally reasonably constant over time, the overall levels of wastewater are affected by weather conditions. For example, the levels are higher when the levels of rainfall are high. In order to account for this during analysis, the samples to be analysed for viruses are flow-weighted. This means that the amount of wastewater collected and analysed relates to the flow of incoming wastewater. More information on this can be found in Hellmér et al. (2014) and Wang et al. (2022). At the Clinical Microbiology Laboratory, two methods developed in-house were used to concentrate viruses. The current method used involves ultrafiltration as the main concentration method. Our previous method used an electropositive filter (Argonide, Florida, USA) as the primary means of concentration (Saguti et al., 2021). Nucleic acids are extracted from 1ml of the concentrated sample using the QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Real-time quantitative PCR (RT-qPCR) is performed to detect and quantify the viral genomes. Details about the method of calculation are provided in Hellmér et al. (2014), Saguti et al. (2021), Wang et al. (2022), and Wang et al. (2023). With both techniques, the amounts of the different virus genomes are given as daily average amounts, as they are based on one week of wastewater sampling."
        }},
        {{
          "name": "data_source",
          "value": "Gothenburg University"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/wastewater/enteric_quantification/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset17"
        }},
        {{
          "name": "name",
          "value": "Historic data for enteric virus quantification in wastewater (Gothenburg University)"
        }},
        {{
          "name": "description",
          "value": "The data was collected between week 2 and week 43 of 2023. An updated method started to be used as of week 20 of 2023. Multiple enteric viruses were quantified; enterovirus, adenovirus, GG2, astrovirus, and sapovirus."
        }},
        {{
          "name": "updated_date",
          "value": "23-11-17"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Wastewater"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "Enteric viruses"
        }},
        {{
          "name": "methods",
          "value": "Samples of wastewater were collected using a fixed-site sampler that collects 30ml per 10,000m3 of the incoming wastewater. For the purposes of analysis, seven samples (each representing a 24 hour period) were pooled to create a weekly sample. Part of this weekly sample was sent to the Clinical Microbiology Laboratory at Sahlgrenska University Hospital for analysis. The amount of sample sent varies between 1.5-15l of wastewater depending on the flow, which is determined in large part by the weather. Whilst the amount of wastewater from households and industry is generally reasonably constant over time, the overall levels of wastewater are affected by weather conditions. For example, the levels are higher when the levels of rainfall are high. In order to account for this during analysis, the samples to be analysed for viruses were flow-weighted. This means that the amount of wastewater collected and analysed related to the flow of incoming wastewater. More information on this can be found in Hellmér et al. (2014) and Wang et al. (2022). At the Clinical Microbiology Laboratory, viruses were concentrated to a final volume of 2.5ml using a method that was developed in-house. This method used the NanoCeram electropositive filter (Argonide, Florida, USA) as the primary means of concentration, and then ultracentrifugation as secondary concentration method (Saguti et al., 2021). Nucleic acids were extracted from 1ml of the concentrated sample using the QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Real-time quantitative PCR (RT-qPCR) was performed to detect and quantify the viral genomes. Details about the method of calculation are provided in Hellmér et al. (2014), Saguti et al. (2021), and Wang et al. (2022)."
        }},
        {{
          "name": "data_source",
          "value": "Gothenburg University"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/wastewater/enteric_quantification/historic_enteric_gu/"
        }}
      ]
    }},
    {{
      "fields": [
        {{
          "name": "id",
          "value": "dataset18"
        }},
        {{
          "name": "name",
          "value": "Influenza quantification (SLU)"
        }},
        {{
          "name": "description",
          "value": "Quantification of the levels of influenza (InfA and InfB) in wastewater from multiple sites, including Stockholm, Malmö, Gothenburg, Uppsala, Västerås, Örebro, Umeå, and many others, by the SEEC-SLU node"
        }},
        {{
          "name": "updated_date",
          "value": "{dataset18_modified}"
        }},
        {{
          "name": "country",
          "value": "Sweden"
        }},
        {{
          "name": "data_type",
          "value": "Wastewater"
        }},
        {{
          "name": "type_of_pathogen",
          "value": "Influenza"
        }},
        {{
          "name": "methods",
          "value": "For most cities represented on this page, raw, untreated wastewater samples that are representative of a single day are collected by flow compensated samplers at the wastewater treatment plants (WWTP). Uppsala is the exception, where samples are collected daily, and then combined flow-proportionally into one composite weekly sample for the purpose of analyses. The viral genomic material from the freshly collected samples is extracted by the direct capture method, using the Maxwell RSC Enviro TNA kit (Promega). Absolute quantification of the copy numbers of the genome of influenza A and B viruses is performed by One-Step RT-qPCR using the Flu SC2 Multiplex Assay from the Centers for Disease Control and Prevention (CDC). To correct for variations in population size and wastewater flow, pepper mild mottle virus (PMMoV) is quantified using a modified version of the assay of Zhang et al. (2006). PMMoV is an abundant RNA virus in human faeces and serves as an estimator of human faecal content (Symonds et al., 2019). The data represent the ratio of the copy numbers measured by the Flu SC2 Multiplex Assay and PMMoV-assays, multiplied by 1000. As the Flu SC2 Multiplex Assay provides proxies for both influenza A and B viruses content in the wastewater and PMMoV is a proxy of the faecal content (which is related to the contributing population), their ratio can be considered as a proxy for the prevalence of influenza A and influenza B infections in the population of the wastewater catchment area."
        }},
        {{
          "name": "data_source",
          "value": "Swedish University of Agricultural Sciences (SLU)"
        }},
        {{
          "name": "source_page",
          "value": "https://www.pathogens.se/dashboards/wastewater/influenza_quantification/"
        }}
      ]
    }}
  ]
}}
'''