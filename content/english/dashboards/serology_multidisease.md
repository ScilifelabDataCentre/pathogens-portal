---
title: Multiplex and high-throughput multi-disease serology
description: A summary of the progress in formating a multi-disease serology assay, a key component of pandemic preparedness. Information about commercially available antigens is provided.
banner: /dashboard_thumbs/multi-disease-serology.jpg
toc: false
menu:
  dashboard_menu:
    identifier: multi_disease_serology
    name: Multiplex and high-throughput multi-disease serology
dashboards_topics:
  [COVID-19, Infectious diseases, Influenza, Enteric viruses, Mpox]
toc: true
---

<div class="alert alert-info">
  <i class="bi bi-exclamation-triangle-fill"></i>
  <span>The information on this dashboard will be extended to include testing data when it becomes available.</span>
</div>

## Introduction

The capacity to conduct large-scale surveillance of seroprevalence (i.e. the number of people in a population that test positive for a given disease) is a key component of pandemic preparedness efforts.

The COVID-19 pandemic highlighted the importance of serological surveillance in tracking viral transmission dynamics, understanding immune responses, guiding vaccination strategies, and assisting in decisions related to public health. High-throughput serological assays for SARS-CoV-2 were developed very early in the pandemic to enable surveillance of populations globally. For information about work done with SARS-CoV-2 during the pandemic, see the [historical background section](#historical-background).

As we move on from the pandemic, it is crucial that serological studies include many more pathogens other than SARS-CoV-2. One of the capabilities that is part of [SciLifeLab's Pandemic Laboratory Preparedness (PLP) program](/plp-program-background/), named 'Multiplex and high-throughput multi-disease serology' aims to create a sustainable, long-term resource enabling a broad, frequent, and large-scale surveillance of serostatus. They are working to create antibody repertoires that can be used for thousands of samples based on hundreds of antigens. The project is led by Peter Nilsson at KTH Royal Institute of Technology. To learn more, check out the [pandemic preparedness resource page for this project](/resources/serology/).

This dashboard details the work done as part of the multiplex and high-throughput multi-disease serology study.

## Historical background

During the pandemic, those working on the multiplex and high-throughput multi-disease serology study created a high-throughput multiplex bead-based serological assay for SARS-CoV-2 (see [Hober _et al._ (2021)](https://doi.org/10.1002/cti2.1312) and the [Serology tests for SARS-CoV-2 at SciLifeLab Data Dashboard](/serology-statistics/) for details). As of July 2023, the assay had been used to analyse over 250,000 samples, and contributed to [around 40 publications](https://publications.scilifelab.se/label/Autoimmunity%20and%20Serology%20Profiling), including studies on seroprevalence and on vaccine efficacy in immunocompromised individuals and individuals with autoimmune diseases. Following the pandemic, the group began to refocus their efforts towards pandemic preparedness, and began work to extend the assay to provide a platform for parallelized multi-disease serological studies including a wide range of antigens representing various infectious diseases. The bead-based setup enables a stepwise addition of new proteins, allowing a continuous implementation of pathogen-representing antigens.

## Current methods and progress

In order to expand the previously developed high-throughput multiplex bead-based serological assay for SARS-CoV-2, it is necessary to design and produce molecules that can be used in the assay to detect pathogens.

As of February 2024, the project has designed and produced many molecules. This includes, for example, 155 different variants of the SARS-CoV-2 spike glycoprotein, covering the majority of all variants of interest (VOI) and concern (VOC). The majority of the variants (117) represent SARS--CoV-2 wild type, and 38 represent spike mutation variants (mutations only in the RBD-region). They have also created spike representations of SARS, MERS, and the other four human coronaviruses causing common cold (HKU1, OC43, NL63 and 229E). They have also produced influenza virus antigens representing the glycoproteins hemagglutinin and neuraminidase. Here, they have been initially focused on the variants present in the trivalent vaccine for the season 2021-2022, which includes the A(H1N1)/Wisconsin, A(H3N2)/Cambodia and B(Victoria)/Washington strains. Furthermore, they have produced representations of Respiratory Syncytial Virus (RSV), including two surface proteins (G and F) in two different strains. Antigens representing monkeypox have also been generated and included in the current bead-based antigen collection.

Other viral respiratory infections that are being monitored in Sweden includes adenovirus, metapneumovirus, and parainfluenza virus. There are currently 88 different human adenoviruses divided into seven species, with species B and C primarily causing respiratory diseases. The project has designed representations of the fibre protein of adenovirus B7. Metapneumovirus is closely related to RSV, both when it comes to genomic organisation and clinical features. They have designed representations of proteins F and G of the strain CAN97-83. Lastly, representations of protein HN and F for parainfluenza virus have been designed based on strain Washington/1957 and strain C39, respectively.

The proteins designed and produced created by the project to date are listed in the [below table](#table-of-proteins-created-at-kth).

### Table of proteins created at KTH

Proteins designed, expressed, purified, and characterised at KTH. They have been expressed either in HEK or CHO cells or in _E.scherichia coli_, and either as fragments or full-length proteins.

**CONTACT??**

<div class="table-responsive">
  <table id="variants" class="table table-hover" width="100%">
    <thead class="table-light">
      <tr>
        <th scope="col">Virus Type</th>
        <th scope="col">Variant</th>
        <th scope="col">Comment</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Spike</td>
        <td>Wildtype virus, 20 different variants</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Spike RBD</td>
        <td>Wildtype virus, 10 different variants</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Spike S1</td>
        <td>Wildtype virus, 19 different variants</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Spike S2</td>
        <td>Wildtype virus, 4 different variants</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Nucleocapsid</td>
        <td>Wildtype virus, 17 different variants</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Envelop</td>
        <td>Wildtype virus, 2 different variants</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Membrane</td>
        <td>Wildtype virus, 1 different variants</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>RNA Ploymerase</td>
        <td>Wildtype virus, 1 different variants</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Non-structural proteins (NSP)</td>
        <td>Wildtype virus, 24 different variants</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>ORF proteins</td>
        <td>Wildtype virus, 19 different variants</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Alpha (B.1.1.7)</td>
        <td>Mutation only in the RBD-region</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Beta (B.1.351)</td>
        <td>Mutation only in the RBD-region</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Gamma (P.1)</td>
        <td>Mutation only in the RBD-region</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Delta (B.1.617.2)</td>
        <td>Mutation only in the RBD-region</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Delta plus (B.1.617.2.1)</td>
        <td>Mutation only in the RBD-region</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Eta (B.1.525)</td>
        <td>Mutation only in the RBD-region</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Kappa (B.1.617.1)</td>
        <td>Mutation only in the RBD-region</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Omicron BA.1</td>
        <td>Complete set of mutations</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Omicron BA.2</td>
        <td>Complete set of mutations</td>
      </tr>
      <tr>
        <td>SARS-CoV-2</td>
        <td>Omicron BA.5</td>
        <td>Complete set of mutations</td>
      </tr>
      <tr>
        <td>Other human corona viruses</td>
        <td>SARS-CoV</td>
        <td></td>
      </tr>
      <tr>
        <td>Other human corona viruses</td>
        <td>MERS-CoV</td>
        <td></td>
      </tr>
      <tr>
        <td>Other human corona viruses</td>
        <td>HCoV-229E</td>
        <td></td>
      </tr>
      <tr>
        <td>Other human corona viruses</td>
        <td>HCoV-HKU1</td>
        <td></td>
      </tr>
      <tr>
        <td>Other human corona viruses</td>
        <td>HCoV-NL63</td>
        <td></td>
      </tr>
      <tr>
        <td>Other human corona viruses</td>
        <td>HCoV-OC43</td>
        <td></td>
      </tr>
      <tr>
        <td>Influenza virus</td>
        <td>A/H1N1 HA/Wisconsin/588/2019</td>
        <td></td>
      </tr>
      <tr>
        <td>Influenza virus</td>
        <td>A/H1N1 NA/Wisconsin/588/2019</td>
        <td></td>
      </tr>
      <tr>
        <td>Influenza virus</td>
        <td>A/H3N2 HA/Cambodia/e0826360/2020</td>
        <td></td>
      </tr>
      <tr>
        <td>Influenza virus</td>
        <td>A/H3N2 NA/Cambodia/e0826360/2020</td>
        <td></td>
      </tr>
      <tr>
        <td>Influenza virus</td>
        <td>B/Victoria HA/Washington/02/2019</td>
        <td></td>
      </tr>
      <tr>
        <td>Influenza virus</td>
        <td>B/Victoria NA/Washington/02/2019</td>
        <td></td>
      </tr>
      <tr>
        <td>Respiratory Syncytial Virus (RSV)</td>
        <td>A/A2 Glycoprotein tetramer</td>
        <td></td>
      </tr>
      <tr>
        <td>Respiratory Syncytial Virus (RSV)</td>
        <td>B/18537 Fusion protein</td>
        <td></td>
      </tr>
      <tr>
        <td>Respiratory Syncytial Virus (RSV)</td>
        <td>B/18537 Glycoprotein tetramer</td>
        <td></td>
      </tr>
      <tr>
        <td>Adenovirus</td>
        <td>HAdV-B7</td>
        <td>Fiber protein (aka spike protein)</td>
      </tr>
      <tr>
        <td>Parainfluenza</td>
        <td>HPIV-1 strain C39</td>
        <td>F</td>
      </tr>
      <tr>
        <td>Parainfluenza</td>
        <td>HPIV-1 strain Washington/1957</td>
        <td>HN</td>
      </tr>
      <tr>
        <td>Metapneumovirus</td>
        <td>HMPV-A strain CAN97-83</td>
        <td>F</td>
      </tr>
      <tr>
        <td>Metapneumovirus</td>
        <td>HMPV-A strain CAN97-83</td>
        <td>G</td>
      </tr>
      <tr>
        <td>Mpox</td>
        <td>A29L</td>
        <td></td>
      </tr>
      <tr>
        <td>Mpox</td>
        <td>A30L</td>
        <td></td>
      </tr>
      <tr>
        <td>Mpox</td>
        <td>E8L</td>
        <td></td>
      </tr>
      <tr>
        <td>Mpox</td>
        <td>H3L</td>
        <td></td>
      </tr>
    </tbody>
  </table>
</div>

## Ongoing work and collaborations

The work of the project is now expanding into the area of the large families of flavivirus (e.g. the TBE (tick-borne encephalitis), Zikas, dengue, West Nile, and yellow fever viruses) and herpesvirus (e.g. Epstein–Barr virus, chickenpox (varicella), herpes simplex), and also adding bacterial respiratory infectious diseases such as tuberculosis.

The project has is also collaborating with another SciLifeLab PLP project [“Systems-level immunomonitoring to unravel immune response to a novel pathogen”](/resources/immunomonitoring/), headed by Petter Brodin (Karolinska Institutet, KI) and Jochen Schwenk (KTH), to include a long range of commercially available antigens representing a large part of the Swedish vaccination program, see list below. These are listed in the table below.

During the pandemic, the scarcity of reagents posed a major hindrance for testing. To ensure constant access to high-quality antigens in future, the project will produce all antigens in-house. This is done in close collaboration within the Department of Protein Science at KTH. Åsa Sivertsson at the Division of Systems Biology designs the protein and fragments to express. Sophia Hober and Hanna Tegel at the Division of Protein Technology at the KTH node of Protein Production Sweden (PPS), a national research infrastructure funded by the Swedish Research Council, express, purify and quality assure.

The multi-disease serological assay is under constant development and will gradually be incorporated into the SciLifeLab infrastructure unit Autoimmunity and Serology Profiling, headed by Ronald Sjöberg. The goal is to provide a flexible and quickly adaptable assay for studies on seroprevalence available to both the Public Health Agency of Sweden and researchers.

### Commercially available antigens

The commercially available antigens provided by Peter Brodin (KI) and Jochen Schwenk (KTH) represent a significant portion of the Swedish vaccination program.

<div class="table-responsive">
  <table id="antigens" class="table table-hover" width="100%">
    <thead class="table-light">
      <tr>
        <th scope="col">Group</th>
        <th scope="col">Subtype/Linage/Strain</th>
      </tr>
    </thead>
      <tr>
        <td>Pertussis</td>
        <td>Bordetella pertussis Filamentous Hemagglutinin (FHA)</td>
      </tr>
      <tr>
        <td>Pertussis</td>
        <td>Bordetella pertussis Filamentous Hemagglutinin (FHA) - Bulk antigen</td>
      </tr>
      <tr>
        <td>Pertussis</td>
        <td>B. Pertussis toxin (mutant)</td>
      </tr>
      <tr>
        <td>Pertussis</td>
        <td>B. Pertussis Pertactin Protein [His]</td>
      </tr>
      <tr>
        <td>Pertussis</td>
        <td>Bordetella pertussis Filamentous Hemagglutinin (FHA) - Nativeantigen</td>
      </tr>
      <tr>
        <td>Pertussis</td>
        <td>B. Pertussis whole-cell (strain tahoma I)</td>
      </tr>
      <tr>
        <td>Measles</td>
        <td>Measles Virus Nucleoprotein (HEK293)</td>
      </tr>
      <tr>
        <td>Measles</td>
        <td>Native Measles virus</td>
      </tr>
      <tr>
        <td>Rotavirus</td>
        <td>Rotavirus VP7 Protein</td>
      </tr>
      <tr>
        <td>Rotavirus</td>
        <td>RotaVirus (Strain SA-11)</td>
      </tr>
      <tr>
        <td>Rubella</td>
        <td>Rubella virus nucleoprotein, C-terminal His-tag</td>
      </tr>
      <tr>
        <td>Rubella</td>
        <td>Rubella Virus Grade 4, natural antigen.</td>
      </tr>
      <tr>
        <td>Rubella</td>
        <td>Rubella E1</td>
      </tr>
      <tr>
        <td>Rubella</td>
        <td>Rubella virus E1, C-terminal SHFC-tag</td>
      </tr>
      <tr>
        <td>Rubella</td>
        <td>Rubella Spike Ectodomain (E1-E2)</td>
      </tr>
      <tr>
        <td>Diphtheria</td>
        <td>Diphtheria mutated toxin</td>
      </tr>
      <tr>
        <td>Diphtheria</td>
        <td>Diphtheria Toxoid</td>
      </tr>
      <tr>
        <td>Mumps</td>
        <td>Mumps Virus Nucleoprotein Recombinant</td>
      </tr>
      <tr>
        <td>Mumps</td>
        <td>Mumps virus nucleoprotein</td>
      </tr>
      <tr>
        <td>Mumps</td>
        <td>Mumps virus nucleoprotein, inactivated pathogen.</td>
      </tr>
      <tr>
        <td>Mumps</td>
        <td>Native Mumps virus</td>
      </tr>
      <tr>
        <td>Humant Papillomvirus</td>
        <td>HPV type 16 L1 Protein (full length)</td>
      </tr>
      <tr>
        <td>Humant Papillomvirus</td>
        <td>HPV type 18 L1 Protein (full length)</td>
      </tr>
      <tr>
        <td>Humant Papillomvirus</td>
        <td>Recombinant HPV type 6 L1 protein (VLP)</td>
      </tr>
      <tr>
        <td>Humant Papillomvirus</td>
        <td>Recombinant Human Papilloma Virus type 33 L1 protein (VLP)</td>
      </tr>
      <tr>
        <td>Pneumococcus</td>
        <td>S. Pneumoniae Cell Wall Polysaccharide Antigen</td>
      </tr>
      <tr>
        <td>Tetanus</td>
        <td>Clostridium tetani Tetanus Toxoid</td>
      </tr>
      <tr>
        <td>Tetanus</td>
        <td>Tetanus Toxoid, Recombinant Heavy Chain Fragment C</td>
      </tr>
      <tr>
        <td>Hepatit-B</td>
        <td>HBV Surface Antigen (subtype adw)</td>
      </tr>
      <tr>
        <td>Poliovirus </td>
        <td>Recombinant Poliovirus type 1 Capsid protein (strain Sabin)</td>
      </tr>
      <tr>
        <td>Poliovirus </td>
        <td>Recombinant Poliovirus type 2 VP3-VP1 capsid Protein [His]</td>
      </tr>
      <tr>
        <td>Poliovirus </td>
        <td>Recombinant Poliovirus type 3 VP3-VP1 capsid protein</td>
      </tr>
      <tr>
        <td>Cytomegalovirus (CMV)</td>
        <td>Cytomegalovirus glycoprotein B (gB)</td>
      </tr>
      <tr>
        <td>Epstein–Barr virus (EBV)</td>
        <td>Epstein Barr Virus gp125</td>
      </tr>
      <tr>
        <td>Epstein–Barr virus (EBV)</td>
        <td>Epstein–Barr nuclear antigen 1</td>
      </tr>
      <tr>
        <td>Respiratory syncytial</td>
        <td>Respiratory Syncytial Virus A Glycoprotein G</td>
      </tr>
    <tbody>
    </tbody>
  </table>
</div>

<script>
  $(document).ready(function () {
    var tableConfig = {
      "sDom": '<"top row"<"col-md"i><"col-md"f>>rt<"bottom row"<"col-md"l><"col-md"p>><"clear">',
      "order": [],
      "language": {
        "lengthMenu": "Show _MENU_ entries per page",
        "zeroRecords": "Nothing found.",
        "info": "Showing _START_ to _END_ of _TOTAL_ entries.",
        "infoEmpty": "No records available",
        "infoFiltered": "(filtered from _MAX_ total records)",
        "search": "Search:",
        "paginate": {
          "first": "First",
          "last": "Last",
          "next": "»",
          "previous": "«"
        }
      }
    };
    $('#variants').DataTable(tableConfig);
    $('#antigens').DataTable(tableConfig);
  });
</script>

<script type="text/javascript" charset="utf8"
  src="https://cdn.datatables.net/1.13.1/js/jquery.dataTables.min.js"></script>
<script type="text/javascript" charset="utf8"
  src="https://cdn.datatables.net/1.13.1/js/dataTables.bootstrap5.min.js"></script>
