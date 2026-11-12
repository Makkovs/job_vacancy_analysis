import { useEffect, useState } from "react";

import { fetchJobs } from "../../http/jobs";
import type { JobType } from "../../types/jobs";

import Job from "./Job/Job";
import Filters from "./Filters/Filters";
import JobsList from "./JobsList/JobsList";
import Loading from "../components/Loading/Loading";

import styles from "./jobs.module.css";

const Jobs = () => {

  const [jobs, setJobs] = useState<JobType[]>([]);
  const [selectedJob, setSelectedJob] = useState<JobType>();
  const [loading, setLoading] = useState<boolean>(true)

  useEffect(() => {
    fetchJobs().then((data) => {
      if (data) {
        setJobs(data)
        setSelectedJob(data[0])
      }
      setLoading(false);
    });
  }, []);

  return (
    <div className={styles.wrapper}>
      <Job job={selectedJob}/>
      <Filters />
      {loading && <Loading />}
      <JobsList
        jobs={jobs}
        selectedJobId={selectedJob?.id || -1}
        setSelectedJob={setSelectedJob}
      />
    </div>
  );
}

export default Jobs;