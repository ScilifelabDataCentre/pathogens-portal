---
title: Multi-disease serology
description: A summary of the progress in developing a multi-disease serology assay, a key component of pandemic preparedness. Information about externally produced antigens is also provided.
banner: /dashboard_thumbs/multi-disease-serology.jpg
toc: false
menu:
  dashboard_menu:
    identifier: multi_disease_serology
    name: Multi-disease serology
dashboards_topics:
  [COVID-19, Infectious diseases, Influenza, Enteric viruses, Mpox]
toc: true
data_status: "updating" # or "historic"
---

<div class="alert alert-info">All data last updated: 2024-08-05</div>

## Introduction

The COVID-19 pandemic highlighted the importance of serological surveillance in tracking viral transmission dynamics, understanding immune responses, guiding vaccination strategies, and assisting in decisions related to public health. High-throughput serological assays for SARS-CoV-2 were developed very early in the pandemic at KTH and SciLifeLab to enable surveillance of populations globally. For information about work done with SARS-CoV-2 during the pandemic, see the [historical background section](#historical-background).

As we move on from the pandemic, it is crucial that serological studies include more pathogens than just SARS-CoV-2. One of the capabilities that is part of [SciLifeLab's Pandemic Laboratory Preparedness (PLP) program](/plp-program-background/), named 'Multi-disease serology' aims to create a sustainable, long-term resource enabling a broad, frequent, and large-scale surveillance of serostatus. They are working to create antibody repertoires that can be used to analyse thousands of samples on hundreds of antigens. The project is led by Peter Nilsson at KTH Royal Institute of Technology and SciLifeLab. To learn more, check out the [pandemic preparedness resource page for this project](/resources/serology/).

## Historical background

During the pandemic, those working on the multi-disease serology study created a high-throughput multiplex bead-based serological assay for SARS-CoV-2 (see [Hober _et al._ (2021)](https://doi.org/10.1002/cti2.1312) and the [Serology tests for SARS-CoV-2 at SciLifeLab Data Dashboard](/dashboards/serology-statistics/) for details). As of July 2023, the assay had been used to analyse over 250,000 samples, and contributed to [around 40 publications](https://publications.scilifelab.se/label/Autoimmunity%20and%20Serology%20Profiling), including studies on seroprevalence and on vaccine efficacy in immunocompromised individuals and individuals with autoimmune diseases. Following the pandemic, the group began to refocus their efforts towards pandemic preparedness, and began work to extend the assay to provide a platform for parallelised multi-disease serological studies, including a wide range of antigens representing various infectious diseases. The bead-based setup enables a stepwise addition of new proteins, allowing a continuous implementation of pathogen-representing antigens.

## Current methods and progress

The project has produced and evaluated many antigens. This includes a wide range of different variants of the SARS-CoV-2 proteins, with a focus on the spike glycoprotein, also covering the majority of mutated variants. They have also created spike representations of SARS, MERS, and the other four human coronaviruses causing common cold (HKU1, OC43, NL63 and 229E). They have also produced influenza virus antigens representing the glycoproteins hemagglutinin and neuraminidase. Here, they have been initially focused on the variants present in the trivalent vaccine for the season 2021-2022, which includes the A(H1N1)/Wisconsin, A(H3N2)/Cambodia, and B(Victoria)/Washington strains. Furthermore, they have produced representations of Respiratory Syncytial Virus (RSV), including two surface proteins (G and F) in two different strains. Antigens representing monkeypox have also been generated and included in the current bead-based antigen collection.

Other viral respiratory infections that are being monitored in Sweden include adenovirus, metapneumovirus, and parainfluenza virus. These have also been added to the project. The project has designed representations of the fibre protein of adenovirus B7, metapneumovirus proteins F and G of the strain CAN97-83, and protein HN and F for parainfluenza virus have been designed based on strain Washington/1957 and strain C39, respectively.

The proteins designed and produced created by the project to date are listed in the [below table](#table-of-proteins-created-at-kth).

### Table of proteins created at KTH

Proteins designed, expressed, purified, and characterised at the [KTH node of Protein Production Sweden](https://www.kth.se/pps), a national research infrastructure funded by the Swedish Research Council. They have been expressed either in HEK or CHO cells or in _E. coli_, with different affinity tags and either as fragments or full-length proteins.

<div class="d-lg-none alert alert-info">
  Rotating your phone will improve the view of this table.
</div>

<div class="table-responsive">
    <table id="table1" class="table table-hover" width="100%">
        <thead class="table-light">
            <tr>
                <th scope="col">Virus Type</th>
                <th scope="col">Variant</th>
                <th scope="col">Protein</th>
                <th scope="col">Details</th>
                <th scope="col">Host</th>
            </tr>
        </thead>
        <tbody>
            <!-- Data for the table will be dynamically populated here -->
        </tbody>
    </table>
</div>

## Ongoing work and collaborations

The work of the project is now expanding into the area of flavivirus (Tick-borne encephalitis virus, Zika virus, Dengue virus, West Nile virus, Yellow fever virus, Japanese encephalitis virus) and herpesvirus (Epstein–Barr virus, Varicella zoster virus, Herpes simplex virus, Cytomegalovirus).

The project is also collaborating with another SciLifeLab PLP project [“Systems-level immunomonitoring to unravel immune response to a novel pathogen”](/resources/immunomonitoring/), headed by Petter Brodin (Karolinska Institutet, KI) and Jochen Schwenk (KTH), to include a wide range of externally produced antigens representing a large part of the Swedish vaccination program, see list below.

The multi-disease serological assay is under constant development and will gradually be incorporated into two SciLifeLab infrastructure units; [Autoimmunity and Serology Profiling](https://www.scilifelab.se/units/autoimmunity-profiling/) and [Affinity Proteomics Stockholm](https://www.scilifelab.se/units/affinity-proteomics/). The goal is to provide a flexible and quickly adaptable assay for high-throughput multiplex studies on seroprevalence, available to both the Public Health Agency of Sweden and researchers in academia and industry.

### Externally produced antigens

<div class="table-responsive">
    <table id="table2" class="table table-hover" width="100%">
        <thead class="table-light">
            <tr>
                <th scope="col">Pathogen</th>
                <th scope="col">Variant</th>
                <th scope="col">Protein</th>
                <th scope="col">Details</th>
                <th scope="col">Host</th>
            </tr>
        </thead>
        <tbody>
            <!-- Data for the table will be dynamically populated here -->
        </tbody>
    </table>
</div>

<script>
    async function fetchAndPopulateTable(url, tableId, headers) {
        try {
            // Attempt to fetch the file
            const response = await fetch(url);

            // Check if the response is OK
            if (!response.ok) {
                throw new Error("Failed to load data. Please try again later.");
            }

            const arrayBuffer = await response.arrayBuffer();

            // Parse the Excel file
            const workbook = XLSX.read(arrayBuffer, { type: "array" });
            const sheetName = workbook.SheetNames[0]; // Assuming the first sheet
            const worksheet = workbook.Sheets[sheetName];
            const jsonData = XLSX.utils.sheet_to_json(worksheet);

            // Check if the parsed JSON data is empty
            if (jsonData.length === 0) {
                throw new Error("The data is currently unavailable. Please check back later.");
            }

            // Populate the table
            const tableBody = document.getElementById(tableId).querySelector('tbody');
            tableBody.innerHTML = ''; // Clear any existing content

            jsonData.forEach(row => {
                const tr = document.createElement('tr');

                // Create cells for each column based on provided headers
                headers.forEach(column => {
                    const td = document.createElement('td');
                    td.textContent = row[column] || ''; // Display an empty string if the data is missing
                    tr.appendChild(td);
                });

                tableBody.appendChild(tr);
            });

            // Initialize DataTables for this table
            $(`#${tableId}`).DataTable({
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
            });

        } catch (error) {
            console.error(`Error processing table ${tableId}:`, error.message);

            // Display an error message in the table
            const tableBody = document.getElementById(tableId).querySelector('tbody');
            tableBody.innerHTML = `<tr><td colspan="${headers.length}" class="text-center text-danger">An error occurred while loading the data. Please try again later.</td></tr>`;
        }
    }

    // URLs and headers for the two tables
    const tables = [
       {
            url: "https://blobserver.dc.scilifelab.se/blob/KTH-produced-antigens%20240418.xlsx",
            tableId: "table1",
            headers: ['Virus type', 'Variant', 'Protein', 'Details', 'Host']
        },
        {
            url: "https://blobserver.dc.scilifelab.se/blob/External-PLP-proteinlist.xlsx",
            tableId: "table2",
            headers: ['Pathogen', 'Variant', 'Protein', 'Details', 'Host']
        }
    ];

    // Fetch and populate data for both tables when the page loads
    window.onload = function() {
        tables.forEach(table => {
            fetchAndPopulateTable(table.url, table.tableId, table.headers);
        });
    };
</script>


<script type="text/javascript" charset="utf8"
  src="https://cdn.datatables.net/1.13.1/js/jquery.dataTables.min.js"></script>
<script type="text/javascript" charset="utf8"
  src="https://cdn.datatables.net/1.13.1/js/dataTables.bootstrap5.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
