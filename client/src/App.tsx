import styles from "./App.module.css";

function App() {

  return (
    <div className={styles.wrapper}>
      <nav className={styles.filters}>
        Filters
      </nav>
      <div className={styles.main}>
        <div className={styles.job}>
          Job
        </div>
        <div className={styles.jobs_list}>
          Job List
        </div>
      </div>
      <div className={styles.statistic}>
        Statistic
      </div>
    </div>
    
  );
}

export default App;
