import PaymentsIcon from '@mui/icons-material/Payments';
import SchoolIcon from '@mui/icons-material/School';
import WorkIcon from '@mui/icons-material/Work';

import type { JobType, SkillType } from '../../../types/jobs';

import styles from "./job.module.css";

interface JobProps {
  job?: JobType
}

const Job = ({ job }: JobProps) => {
  if (job) {
    return (
      <div className={styles.job}>
        <div>
          <h2>{job.title}</h2>
          <span className={styles.job_country}>{job.country}</span>
        </div>
        <div className={styles.job_main_info}>
          <div className={styles.main_info}>
            <span className={styles.info_icon}>
              <PaymentsIcon fontSize='small' />
            </span>
            <span className={styles.info_title}>Salary</span><br />
            <span className={styles.info_salary}>${job.salary_min} - ${job.salary_max}</span>
          </div>
          <div className={styles.main_info}>
            <span className={styles.info_icon}>
              <WorkIcon fontSize='small' />
            </span>
            <span className={styles.info_title}>Required experience</span><br />
            <span className={styles.info_other}>{job.experience}+ years</span>
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
          {job.skills.map((skill: SkillType) =>
            <span className={styles.job_skill} key={`${job.id}${skill.id}`}>{skill.name}</span>
          )}
        </div>
      </div>
    );
  }
}

export default Job;