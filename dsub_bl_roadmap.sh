#!/bin/bash

dsub \
    --provider google-v2 \
    --project finucane-dp5 \
    --zones "us-east1-b" \
    --disk-size 100 \
    --logging gs://regularized_sldsc/logging/fi_priors/compare_models/ \
    --machine-type n1-highmem-8 \
    --image "gcr.io/finucane-dp5/fi-priors" \
    --script "run_bl_roadmap.py" \
    --task "submit_bl_roadmap_lasso_sample.tsv" \
