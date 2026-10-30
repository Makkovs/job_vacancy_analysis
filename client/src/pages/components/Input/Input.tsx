import SearchIcon from '@mui/icons-material/Search';

import styles from "./input.module.css";

interface InputProps {
  isSearch?: boolean
  className?: string
  placeholder?: string
  type?: string
  value?: string | number
  onChange?: (...args: any[]) => void
}

const Input = ({ className, placeholder, type = "text", isSearch = false }: InputProps) => {
  return (
    <div className={styles.container}>
      <input
        className={
          className ? `${styles.search_input} ${className}`
            : styles.search_input
        }
        type={type}
        placeholder={placeholder || ""}
      />
      {isSearch &&
        <span className={styles.search_icon_input}>
          <SearchIcon fontSize='small' />
        </span>
      }
    </div>
  );
}

export default Input;