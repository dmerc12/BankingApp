import { useContext } from "react";
import { ToastContext } from "../components/ui/toast/toast-context";

export const useToast = () => useContext(ToastContext);