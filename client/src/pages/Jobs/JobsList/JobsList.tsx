import styles from "./jobs_list.module.css";

const JobsList = () => {

  return (
    <div className={styles.jobs_list}>
      <div className={styles.job}>
        <div className={styles.job_row_salary}>
          <span className={styles.salary}>$2,200 - $3,200</span>
        </div>
        <div className={styles.job_row}>
          <h3>Middle UI\UX Developer</h3>
        </div>
        <span className={styles.job_country}>Ukraine</span><br />
        <div className={styles.job_row}>
          <span><span className={styles.info_title}>Experience:</span> 3+ years</span>
          <span><span className={styles.info_title}>Education:</span> None</span>
        </div>
        <div className={styles.skills_list}>
          <span className={styles.skill}>TypeScript</span>
          <span className={styles.skill}>React.js</span>
          <span className={styles.skill}>HTML</span>
        </div>
      </div>
      <div className={styles.job}>
        <div className={styles.job_row_salary}>
          <span className={styles.salary}>$2,200 - $3,200</span>
        </div>
        <div className={styles.job_row}>
          <h3>Middle UI\UX Developer</h3>
        </div>
        <span className={styles.job_country}>Ukraine</span><br />
        <div className={styles.job_row}>
          <span><span className={styles.info_title}>Experience:</span> 3+ years</span>
          <span><span className={styles.info_title}>Education:</span> None</span>
        </div>
        <div className={styles.skills_list}>
          <span className={styles.skill}>TypeScript</span>
          <span className={styles.skill}>React.js</span>
          <span className={styles.skill}>HTML</span>
        </div>
      </div>
      <div className={styles.job}>
        <div className={styles.job_row_salary}>
          <span className={styles.salary}>$2,200 - $3,200</span>
        </div>
        <div className={styles.job_row}>
          <h3>Middle UI\UX Developer</h3>
        </div>
        <span className={styles.job_country}>Ukraine</span><br />
        <div className={styles.job_row}>
          <span><span className={styles.info_title}>Experience:</span> 3+ years</span>
          <span><span className={styles.info_title}>Education:</span> None</span>
        </div>
        <div className={styles.skills_list}>
          <span className={styles.skill}>TypeScript</span>
          <span className={styles.skill}>React.js</span>
          <span className={styles.skill}>HTML</span>
        </div>
      </div>
    </div>
  );
}

export default JobsList;