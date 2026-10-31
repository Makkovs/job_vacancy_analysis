import Job from "./Job/Job";
import Filters from "./Filters/Filters";
import JobsList from "./JobsList/JobsList";

import styles from "./jobs.module.css";


const Jobs = () => {

  return (
    <div className={styles.wrapper}>
      <Job />
      <Filters />
      <JobsList />
    </div>
  );
}

export default Jobs;