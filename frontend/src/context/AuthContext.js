import React, { createContext } from "react";

const AuthContext = createContext(undefined);


const AuthProvider = ({ children }) => {
    return (
        <AuthContext.Provider value={{ name: "Nikita" }}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthProvider;