import SearchIcon from '@mui/icons-material/Search';

import styles from "./input.module.css";

const Input = ({}) => {
  return (
    <div className={styles.container}>
      <input
        className={styles.search_input}
        type="text"
        placeholder="Search..."
      />
      <span className={styles.search_icon_input}>
        <SearchIcon fontSize='small' />
      </span>
    </div>
  );
}

export default Input;