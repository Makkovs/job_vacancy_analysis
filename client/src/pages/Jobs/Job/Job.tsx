import PaymentsIcon from '@mui/icons-material/Payments';
import SchoolIcon from '@mui/icons-material/School';
import WorkIcon from '@mui/icons-material/Work';

import styles from "./job.module.css";

const Job = () => {

  return (
    <div className={styles.job}>
      <div>
        <h2>Senior Lead Full-Stack Developer</h2>
        <span className={styles.job_country}>Germany</span>
      </div>
      <div className={styles.job_main_info}>
        <div className={styles.main_info}>
          <span className={styles.info_icon}>
            <PaymentsIcon fontSize='small' />
          </span>
          <span className={styles.info_title}>Salary</span><br />
          <span className={styles.info_salary}>$4500 - $6000</span>
        </div>
        <div className={styles.main_info}>
          <span className={styles.info_icon}>
            <WorkIcon fontSize='small' />
          </span>
          <span className={styles.info_title}>Required experience</span><br />
          <span className={styles.info_other}>5+ years</span>
        </div>
        <div className={styles.main_info}>
          <span className={styles.info_icon}>
            <SchoolIcon fontSize='small' />
          </span>
          <span className={styles.info_title}>Education</span><br />
          <span className={styles.info_other}>Bachelor's degree</span>
        </div>
      </div>
      <div className={styles.job_skills}>
        <span className={styles.job_skill}>TypeScript</span>
        <span className={styles.job_skill}>React.js</span>
        <span className={styles.job_skill}>HTML</span>
        <span className={styles.job_skill}>CSS</span>
        <span className={styles.job_skill}>PostgreSQL</span>
        <span className={styles.job_skill}>Nest.js</span>
      </div>
    </div>
  );
}

export default Job;