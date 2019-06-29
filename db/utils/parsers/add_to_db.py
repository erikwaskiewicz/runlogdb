import sqlite3



DB = '/data/diagnostics/apps/RunlogDB/RunlogDB-0.1.1/runlog/runlogdb.sqlite3'


def runinfo_add(runinfo_dict, samplesheet_dict, interop_dict):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute(''' INSERT INTO db_runlog (
            run_id, 
            instrument, 
            instrument_date, 
            num_cycles1,
            num_cycles2, 
            investigator, 
            experiment, 
            read1, 
            read2,
            samplesheet_date, 
            workflow, 
            application, 
            assay, 
            description, 
            chemistry,
            plates,
            description2,
            samples,
            I7,
            I5,
            pipeline,
            percent_Q30,
            cluster_density,
            percent_pf,
            phasing,
            prephasing,
            error_rate,
            percent_aligned,
            diagnostic_run
            )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''',
            (runinfo_dict["Id"],
            runinfo_dict["Instrument"],
            runinfo_dict["Date"],
            runinfo_dict["num_cycles1"],
            runinfo_dict["num_cycles2"],
            samplesheet_dict["Investigator Name"],
            samplesheet_dict["Experiment Name"],
            runinfo_dict["read1"],
            runinfo_dict["read2"],
            samplesheet_dict["Date"],
            samplesheet_dict["Workflow"],
            samplesheet_dict["Application"],
            samplesheet_dict["Assay"],
            samplesheet_dict["Description"],
            samplesheet_dict["Chemistry"],
            #samplesheet_dict["Plates"],
            #samplesheet_dict["Description2"],
            #samplesheet_dict["Samples"],
            #samplesheet_dict["I7"],
            #samplesheet_dict["I5"],
            samplesheet_dict["Pipeline"],
            interop_dict["Percent Q30"],
            interop_dict["Cluster density"],
            interop_dict["Percent PF"],
            interop_dict["Phasing"],
            interop_dict["Prephasing"],
            interop_dict["Error rate"],
            interop_dict["Aligned"],
            True))
    db.commit()
    db.close()

'''
Header":{
    "IEMFileVersion":"4",
    "Investigator_Name":"Hoi Ping Weeks-NHS",
    "Experiment_Name":"18-9110_18-9118",
    "Workflow":"GenerateFASTQ",
    "Application":"FASTQ Only",
    "Chemistry":"Default"
  "Reads":{
    "read1":"151",
    "read2":"151"

note: these are pulled out from samplesheet- does it need to be added to database when already pulled?

'''

#------------------------------------------------------------------------------------------------------------------

def worksheetinfo_add(runinfo_dict, samplesheet_dict, ws_dict):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute(''' INSERT INTO db_worksheet (
            ws_id,
            run_id,
            pipelineName,
            pipelineVersion,
            panel
            )
        VALUES(?, ?, ?, ?, ?) ''',
            (samplesheet_dict["Plates"], #duplicate
            runinfo_dict["Id"],            
            ws_dict["Sample_Plate"],    #duplicate 
            ws_dict["pipelineName"],
            ws_dict["pipelineVersion"],
            ws_dict["panel"]

            ))
    db.commit()
    db.close()



def sampleinfo_add(runinfo_dict, samplesheet_dict, sample_dict):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute(''' INSERT INTO db_sample (
        UniqueID,
        ws_id,
        run_id,
        sample_id,
        I7,
        I5, 
        description,
        sample_well,
        sample_project,
        sex
        )
    VALUES(?, ?, ?, ?, ?, ?, ?) ''',
        ( runinfo_dict["Id"] + "_" + samplesheet_dict["Samples"],
        samplesheet_dict["Plates"],
        runinfo_dict["Id"],
        samplesheet_dict["Samples"],
        samplesheet_dict["I7"],
        samplesheet_dict["I5"],
        samplesheet_dict["Description2"],
        sample_dict["Sample_Well"],
        sample_dict["Sample_Project"],
        sample_dict["sex"]
        ))
    db.commit()
    db.close()
    

def miseq_add(dictionary):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute(''' INSERT INTO db_miseq (
            run_id_id, 
            MCS_version, 
            RTA_version, 
            flowcell_serial_no, 
            flowcell_part_no, 
            flowcell_expiry, 
            PR2_serial_no, 
            PR2_part_no, 
            PR2_expiry,
            reagent_serial_no, 
            reagent_part_no, 
            reagent_expiry
            )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''',
           (dictionary["RunID"],
            dictionary["MCSVersion"],
            dictionary["RTAVersion"],
            dictionary["FlowcellRFIDTagSerialNumber"],
            dictionary["FlowcellRFIDTagPartNumber"],
            dictionary["FlowcellRFIDTagExpirationDate"],
            dictionary["PR2BottleRFIDTagSerialNumber"],
            dictionary["PR2BottleRFIDTagPartNumber"],
            dictionary["PR2BottleRFIDTagExpirationDate"],
            dictionary["ReagentKitRFIDTagSerialNumber"],
            dictionary["ReagentKitRFIDTagPartNumber"],
            dictionary["ReagentKitRFIDTagExpirationDate"]))
    db.commit()
    db.close()


def hiseq_add(dictionary):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute(''' INSERT INTO db_hiseq (
            run_id_id, 
            workflow_type,
            paired_end,
            flowcell_version,
            sbs_version,
            pe_version,
            index_version,
            clustering_choice,
            rapid_run_chemistry,
            run_mode,
            application_name,
            application_version,
            FPGA_version,
            CPLD_version,
            RTA_version,
            chemistry_version,
            camera_firmware,
            camera_driver,
            sbs_reagent_kit,
            index_reagent_kit
            )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''',
           (dictionary["RunID"],
            dictionary["WorkFlowType"],
            dictionary["PairEndFC"],
            dictionary["Flowcell"],
            dictionary["Sbs"],
            dictionary["Pe"],
            dictionary["Index"],
            dictionary["ClusteringChoice"],
            dictionary["RapidRunChemistry"],
            dictionary["RunMode"],
            dictionary["ApplicationName"],
            dictionary["ApplicationVersion"],
            dictionary["FPGAVersion"],
            dictionary["CPLDVersion"],
            dictionary["RTAVersion"],
            dictionary["ChemistryVersion"],
            dictionary["CameraFirmware"],
            dictionary["CameraDriver"],
            dictionary["SbsSbsReagentKit"],
            dictionary["IndexReagentKit"]))
    db.commit()
    db.close()


def nextseq_add(dictionary):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute(''' INSERT INTO db_nextseq (
            run_id_id,
            instrument_id,
            RTA_version,
            systemsuite_version,
            flowcell_serial,
            PR2_serial_no,
            reagent_serial_no,
            experiment_name,
            library_id,
            chemistry,
            focus_method,
            surface_to_scan,
            paired_end,
            custom_R1_primer,
            custom_R2_perimer,
            custom_index_primer,
            custom_index2_primer,
            uses_custom_R1_primer,
            uses_custom_R2_perimer,
            uses_custom_index_primer,
            uses_custom_index2_primer,
            run_management_type,
            basespace_id,
            basespace_runmode,
            computer_name,
            max_reagent_kit_cycles,
            application_name,
            application_version
            )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''',
           (dictionary["RunID"],
            dictionary["InstrumentID"],
            dictionary["RTAVersion"],
            dictionary["SystemSuiteVersion"],
            dictionary["FlowCellSerial"],
            dictionary["PR2BottleSerial"],
            dictionary["ReagentKitSerial"],
            dictionary["ExperimentName"],
            dictionary["LibraryID"],
            dictionary["Chemistry"],
            dictionary["FocusMethod"],
            dictionary["SurfaceToScan"],
            dictionary["IsPairedEnd"],
            dictionary["CustomReadOnePrimer"],
            dictionary["CustomReadTwoPrimer"],
            dictionary["CustomIndexPrimer"],
            dictionary["CustomIndexTwoPrimer"],
            dictionary["UsesCustomReadOnePrimer"],
            dictionary["UsesCustomReadTwoPrimer"], 
            dictionary["UsesCustomIndexPrimer"],
            dictionary["UsesCustomIndexTwoPrimer"], 
            dictionary["RunManagementType"],
            dictionary["BaseSpaceRunId"],
            dictionary["BaseSpaceRunMode"], 
            dictionary["ComputerName"],
            dictionary["MaxCyclesSupportedByReagentKit"],
            dictionary["ApplicationName"],
            dictionary["ApplicationVersion"]))
    db.commit()
    db.close()

def SampleMetrics_add(hsdict, runinfo_dict, samplesheet_dict):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute(''' INSERT INTO db_samplemetrics (
            UniqueID, 
            run_id_id,
            SampleID,
            BAIT_SET,
            GENOME_SIZE,
            BAIT_TERRITORY,
            TARGET_TERRITORY,
            BAIT_DESIGN_EFFICIENCY,
            TOTAL_READS,
            PF_READS,
            PF_UNIQUE_READS,
            PCT_PF_READS,
            PCT_PF_UQ_READS,
            PF_UQ_READS_ALIGNED,
            PCT_PF_UQ_READS_ALIGNED,
            PF_BASES_ALIGNED,
            PF_UQ_BASES_ALIGNED,
            ON_BAIT_BASES,
            NEAR_BAIT_BASES,
            OFF_BAIT_BASES,
            ON_TARGET_BASES,
            PCT_SELECTED_BASES,
            PCT_OFF_BAIT,
            ON_BAIT_VS_SELECTED,
            MEAN_BAIT_COVERAGE,
            MEAN_TARGET_COVERAGE,
            MEDIAN_TARGET_COVERAGE,
            MAX_TARGET_COVERAGE,
            PCT_USABLE_BASES_ON_BAIT,
            PCT_USABLE_BASES_ON_TARGET,
            FOLD_ENRICHMENT,
            ZERO_CVG_TARGETS_PCT,
            PCT_EXC_DUPE,
            PCT_EXC_MAPQ,
            PCT_EXC_BASEQ,
            PCT_EXC_OVERLAP,
            PCT_EXC_OFF_TARGET,
            FOLD_80_BASE_PENALTY,
            PCT_TARGET_BASES_1X,
            PCT_TARGET_BASES_2X,
            PCT_TARGET_BASES_10X,
            PCT_TARGET_BASES_20X,
            PCT_TARGET_BASES_30X,
            PCT_TARGET_BASES_40X,
            PCT_TARGET_BASES_50X,
            PCT_TARGET_BASES_100X,
            HS_LIBRARY_SIZE,
            HS_PENALTY_10X,
            HS_PENALTY_20X,
            HS_PENALTY_30X,
            HS_PENALTY_40X,
            HS_PENALTY_50X,
            HS_PENALTY_100X,
            AT_DROPOUT,
            GC_DROPOUT,
            HET_SNP_SENSITIVITY,
            HET_SNP_Q
            )
 
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''',
            (runinfo_dict["Id"] + "_" + samplesheet_dict["Samples"],
            hsdict["run_id"],
            hsdict["SampleID"],
            hsdict["BAIT_SET"],
            hsdict["GENOME_SIZE"],
            hsdict["BAIT_TERRITORY"],
            hsdict["TARGET_TERRITORY"],
            hsdict["BAIT_DESIGN_EFFICIENCY"],
            hsdict["TOTAL_READS"],
            hsdict["PF_READS"],
            hsdict["PF_UNIQUE_READS"],
            hsdict["PCT_PF_READS"],
            hsdict["PCT_PF_UQ_READS"],
            hsdict["PF_UQ_READS_ALIGNED"],
            hsdict["PCT_PF_UQ_READS_ALIGNED"],
            hsdict["PF_BASES_ALIGNED"],
            hsdict["PF_UQ_BASES_ALIGNED"],
            hsdict["ON_BAIT_BASES"],
            hsdict["NEAR_BAIT_BASES"],
            hsdict["OFF_BAIT_BASES"],
            hsdict["ON_TARGET_BASES"],
            hsdict["PCT_SELECTED_BASES"],
            hsdict["PCT_OFF_BAIT"],
            hsdict["ON_BAIT_VS_SELECTED"],
            hsdict["MEAN_BAIT_COVERAGE"],
            hsdict["MEAN_TARGET_COVERAGE"],
            hsdict["MEDIAN_TARGET_COVERAGE"],
            hsdict["MAX_TARGET_COVERAGE"],
            hsdict["PCT_USABLE_BASES_ON_BAIT"],
            hsdict["PCT_USABLE_BASES_ON_TARGET"],
            hsdict["FOLD_ENRICHMENT"],
            hsdict["ZERO_CVG_TARGETS_PCT"],
            hsdict["PCT_EXC_DUPE"],
            hsdict["PCT_EXC_MAPQ"],
            hsdict["PCT_EXC_BASEQ"],
            hsdict["PCT_EXC_OVERLAP"],
            hsdict["PCT_EXC_OFF_TARGET"],
            hsdict["FOLD_80_BASE_PENALTY"],
            hsdict["PCT_TARGET_BASES_1X"],
            hsdict["PCT_TARGET_BASES_2X"],
            hsdict["PCT_TARGET_BASES_10X"],
            hsdict["PCT_TARGET_BASES_20X"],
            hsdict["PCT_TARGET_BASES_30X"],
            hsdict["PCT_TARGET_BASES_40X"],
            hsdict["PCT_TARGET_BASES_50X"],
            hsdict["PCT_TARGET_BASES_100X"],
            hsdict["HS_LIBRARY_SIZE"],
            hsdict["HS_PENALTY_10X"],
            hsdict["HS_PENALTY_20X"],
            hsdict["HS_PENALTY_30X"],
            hsdict["HS_PENALTY_40X"],
            hsdict["HS_PENALTY_50X"],
            hsdict["HS_PENALTY_100X"],
            hsdict["AT_DROPOUT"],
            hsdict["GC_DROPOUT"],
            hsdict["HET_SNP_SENSITIVITY"],
            hsdict["HET_SNP_Q"]))
    db.commit()
    db.close()






def Fastqc_add(dictionary, runinfo_dict, samplesheet_dict):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute(''' INSERT INTO db_fastqc (
            UniqueID_id,
            Read_Group,
            Lane,
            Basic_Statistics,
            Per_base_sequence_quality,
            Per_tile_sequence_quality,
            Per_sequence_quality_scores,
            Per_base_sequence_content,
            Per_sequence_GC_content,
            Per_base_N_content,
            Sequence_Length_Distribution,
            Sequence_Duplication_Levels,
            Overrepresented_sequences,
            Adapter_Content,
            Kmer_Content
            )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''',
           (runinfo_dict["Id"] + "_" + samplesheet_dict["Samples"],
            dictionary["Read_Group"],
            dictionary["Lane"],
            dictionary["Basic Statistics"],
            dictionary["Per base sequence quality"],
            dictionary["Per tile sequence quality"],
            dictionary["Per sequence quality scores"],
            dictionary["Per base sequence content"],
            dictionary["Per sequence GC content"],
            dictionary["Per base N content"],
            dictionary["Sequence Length Distribution"],
            dictionary["Sequence Duplication Levels"],
            dictionary["Overrepresented sequences"],
            dictionary["Adapter Content"],
            dictionary["Kmer Content"]))
    db.commit() 
    db.close()


