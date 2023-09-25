import React, { useState, useEffect } from 'react';
import Snackbar from '@mui/material/Snackbar';
import Alert from '@mui/lab/Alert';

export const CustomSnackbar = ({ message, type }) => {
  const [snackbarOpen, setSnackbarOpen] = useState(false);

  useEffect(() => {
    if (message && type) {
      handleOpenSnackbar();
    }
  }, [message, type]);

  const handleOpenSnackbar = () => {
    setSnackbarOpen(true);
  };

  const handleCloseSnackbar = () => {
    setSnackbarOpen(false);
  };

  return (
    <Snackbar
      anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
      open={snackbarOpen}
      autoHideDuration={6000}
      onClose={handleCloseSnackbar}
    >
      <Alert onClose={handleCloseSnackbar} severity={type}>
        {message}
      </Alert>
    </Snackbar>
  );
};
