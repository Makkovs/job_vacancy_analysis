import SearchIcon from '@mui/icons-material/Search';

import SearchSelect from '../../components/SearchSelect/SearchSelect';
import Input from '../../components/Input/Input';

import styles from "./filters.module.css";

const Filters = () => {

  return (
    <div className={styles.filters}>
      <h2>Search and filtration</h2>
      <div className={styles.filter_options}>
        <div className={styles.filters_input}>
          <span className={styles.filter_input_title}>Salary from</span>
          <Input
            className={styles.salary_input}
            placeholder='Salary'
            type='number'
          />
        </div>
        <div className={styles.filters_input}>
          <span className={styles.filter_input_title}>Salary to</span>
          <Input
            className={styles.salary_input}
            placeholder='Salary'
            type='number'
          />
        </div>
        <div className={styles.filters_input}>
          <span className={styles.filter_input_title}>Experience</span>
          <Input
            className={`${styles.salary_input} ${styles.experience_input}`}
            placeholder='min'
            type='number'
          />
        </div>
        <div className={styles.filters_input}>
          <span className={styles.filter_input_title}>Education</span>
          <select className={styles.filters_select} name="" id="">
            <option value="">None</option>
            <option value="">Bachelor</option>
            <option value="">Master</option>
            <option value="">Doctorate</option>
          </select>
        </div>
      </div>
      <div className={styles.filter_options}>
        <Input isSearch={true} placeholder='Search...' />
        <SearchSelect />
        <SearchSelect />
      </div>
      <div className={styles.selected_skills}>
        <span className={styles.selected_skill}>TypeScript</span>
        <span className={styles.selected_skill}>React.js</span>
        <span className={styles.selected_skill}>HTML</span>
      </div>
      <div className={styles.filters_footer}>
        <div className={styles.search_button}>
          <span className={styles.search_icon}>
            <SearchIcon fontSize='small' />
          </span>
          Search
        </div>
      </div>
    </div>
  );
}

export default Filters;