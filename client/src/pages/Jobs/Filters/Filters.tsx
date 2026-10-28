import SearchIcon from '@mui/icons-material/Search';
import Input from '../../../UI/Input/Input';

import styles from "./filters.module.css";
import SearchSelect from '../../../UI/SearchSelect/SearchSelect';

const Filters = () => {

  return (
    <div className={styles.filters}>
      <h2>Search and filtration</h2>
      <div className={styles.filter_options}>
        <Input />
        <SearchSelect />
        <div className={styles.search_button}>
          <span className={styles.search_icon}>
            <SearchIcon fontSize='small' />
          </span>
          Search
        </div>
      </div>
      <div className={styles.selected_skills}>
        <span className={styles.selected_skill}>TypeScript</span>
        <span className={styles.selected_skill}>React.js</span>
        <span className={styles.selected_skill}>HTML</span>
      </div>
    </div>
  );
}

export default Filters;