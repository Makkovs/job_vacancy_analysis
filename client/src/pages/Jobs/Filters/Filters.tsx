import SearchIcon from '@mui/icons-material/Search';

import styles from "./filters.module.css";

const Filters = () => {

  return (
      <div className={styles.filters}>
        <h2>Search and filtration</h2>
        <div className={styles.search_button}>
        <span className={styles.search_icon}>
          <SearchIcon fontSize='small'/>
        </span>
        Search
        </div>
      </div>
    );
}

export default Filters;