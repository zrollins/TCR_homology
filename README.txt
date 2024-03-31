This repo contains analysis code for scRNAseq of TCRs from CRC patients, protein-protein structure prediction of the TCR-pMHC complex, and the analysis of molecular dynamics descriptors (hydrogen bonds & Lennard-Jones contacts) used to rank patient-specific TCRs to the CEA neoantigen.

![image info](pics/fig1.png)

```
@article{rollins2024,
        title = {Automated protein-protein structure prediction of the T cell receptor-peptide major histocompatibility complex},
        journal = {biorxiv},
        author = {Rollins, Zachary A and Curtis, Matthew B, and Faller, Roland, George, Steven C},
	      url = {https://www.biorxiv.org/content/10.1101/2022.06.01.494331v1},
        month = apr,
        year = {2024}}
```
# TCR single cell RNA sequencing and V(D)J analysis
- 'TCR_scRNA_VDJseq_rscripts.tx' (written in R)

# TCR template files for protein-protein structure prediction
- align_template.rtf (template for Modeller10.1)
- TCR0001.csv (tempalte for ColabFold1.2)

# protein-protein structure prediction scripts
- ColabFold_recycles.sh (script to execute ColabFold1.2)
- TCR_CDR3_Modeller.py (script to execute Modeller10.1)

#  molecular dynamics based descriptors for predicting TCR-pMHC bidning rank
- rmsf.py (Figure 3)
- CartesianCoordinates3.py (Figure 3)
- bond_freq.py (Figure 4, S6)
- bond_freq_plt.py (Figure 4, S6)
- cont_freq.py (Figure 4, S7)
- cont_freq_plt.py (Figure 4, S7)
- bond_stats.py (Figure 4)
- TCR_rmsd.py (Figure S1)
- eq_time (Figure S1)
- clusters.py (Figure S2)
- rmsd_matrix_obj.py (Figure S3-S5)
- rmsd_matrix_plt.py (Figure S3-S5)

# machine learning based methods for predicting TCR-pMHC binding rank
- ml_predictions/ERGOII_AE_VDJdb.csv
- ml_predictions/ERGOII_LSTM_McPAS.csv
- ml_predictions/nettcr2.2_predictions.csv
- ml_predictions/pMTnet_OMNI_prediction.csv
- ml_predictions/pMTNet_prediction.csv

