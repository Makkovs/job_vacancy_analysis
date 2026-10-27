import Job from "./Job/Job";
import Filters from "./Filters/Filters";

import styles from "./jobs.module.css";


const Jobs = () => {

  return (
    <div className={styles.wrapper}>
      <Job />
      <Filters />
    </div>
  );
}

export default Jobs;