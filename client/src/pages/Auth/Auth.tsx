import { useState } from "react";
import Input from "../components/Input/Input";
import styles from "./auth.module.css";

const Auth = () => {

  const [isLogin, setIsLogin] = useState<boolean>(true);

  return (
    <div className={styles.wrapper}>
      <div className={styles.auth}>
        {isLogin ?
          <h2 className={styles.title}>Sign in</h2>
          :
          <h2 className={styles.title}>Sign up</h2>
        }
        <Input
          className={styles.auth_input}
          placeholder="email"
        />
        <Input
          className={styles.auth_input}
          placeholder="password"
        />
        {!isLogin &&
          <Input
            className={styles.auth_input}
            placeholder="confirm password"
          />
        }
        <span className={styles.auth_message}>
          Don't have an account?
          {isLogin ?
            <span
              className={styles.auth_ref}
              onClick={() => setIsLogin(false)}
            >
              Sign up
            </span>
            :
            <span
              className={styles.auth_ref}
              onClick={() => setIsLogin(true)}
            >
              Sign in
            </span>
          }
        </span>
        {isLogin ?
          <div
            className={styles.button}
          >
            Sign In
          </div>
          :
          <div
            className={styles.button}
          >
            Sign Up
          </div>
        }
      </div>
    </div>
  );
}

export default Auth;