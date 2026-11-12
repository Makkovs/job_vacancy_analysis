import type { JobType, SkillType } from "../../../types/jobs";
import styles from "./jobs_list.module.css";

interface JobListProps {
  jobs: JobType[];
  selectedJobId: number;
  setSelectedJob: (job: JobType) => void;
}

const JobsList = ({ jobs, selectedJobId, setSelectedJob }: JobListProps) => {

  return (
    <div className={styles.jobs_list}>
      {jobs.map((job: JobType) =>
        <div
          className={
            selectedJobId == job.id ? `${styles.job} ${styles.selected_job}` : styles.job
          }
          key={job.id}
          onClick={() => setSelectedJob(job)}
        >
          <div className={styles.job_row_salary}>
            <span className={styles.salary}>${job.salary_min} - ${job.salary_max}</span>
          </div>
          <div className={styles.job_row}>
            <h3>{job.title}</h3>
          </div>
          <span className={styles.job_country}>{job.country}</span><br />
          <div className={styles.job_row}>
            <span>
              <span className={styles.info_title}>Experience:</span> {job.experience}+ years
            </span>
            <span>
              <span className={styles.info_title}>Education:</span> None
            </span>
          </div>
          <div className={styles.skills_list}>
            {job.skills?.slice(0, 4).map((skill: SkillType) =>
              <span className={styles.skill} key={`${job.id}${skill.id}`}>
                {skill.name}
              </span>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default JobsList;