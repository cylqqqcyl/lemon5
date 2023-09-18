import React, { useState } from 'react';
import { Box, Button, Stack, Typography } from '@mui/material';
import NavigateBeforeIcon from '@mui/icons-material/NavigateBefore';
import NavigateNextIcon from '@mui/icons-material/NavigateNext';
import FirstPageIcon from '@mui/icons-material/FirstPage';
import LastPageIcon from '@mui/icons-material/LastPage';
import { VoicesCard } from './voices-card';

const attributes = {age: '成年', gender: '女性', accent: '河南话', style: '普通', mood: '开心'} // For testing

export const VoicesGrid = ({selectedIndex, onCardClick}) => {
    const [currentPage, setCurrentPage] = useState(1);
    const rowsPerPage = 5;
    const totalRows = 40;
    const startRow = (currentPage - 1) * rowsPerPage + 1;
    const endRow = Math.min(currentPage * rowsPerPage, totalRows);
    const totalPages = Math.ceil(totalRows / rowsPerPage);
    const handlePageChange = (page) => {
        setCurrentPage(page);
      };

    const handleNextPage = () => {
    if (currentPage < totalPages) {
        setCurrentPage(currentPage + 1);
    }
    };

    const handlePreviousPage = () => {
    if (currentPage > 1) {
        setCurrentPage(currentPage - 1);
    }
    };

    const handleFirstPage = () => {
    setCurrentPage(1);
    };

    const handleLastPage = () => {
    setCurrentPage(totalPages);
    };

  return (
    <Box sx={{ p: 0, py:2 }}>
      <Stack spacing={2}>
        {/* Rows */}
        {Array.from({ length: rowsPerPage }, (_, index) => (
            <VoicesCard key={index} index={index} 
            page={currentPage} rowsPerPage={rowsPerPage} 
            attributes={attributes}
            onClick={() => onCardClick(index + 1 + (currentPage - 1) * rowsPerPage)} />
        ))}
      </Stack>

      {/* Pagination */}
      <Stack direction="row" justifyContent="center" alignItems="center" spacing={2} sx={{ mt: 2 }}>
        <Button variant="contained" disabled={currentPage === 1} onClick={handleFirstPage} sx={{ minWidth: 'auto' }}>
          <FirstPageIcon />
        </Button>
        <Button variant="contained" disabled={currentPage === 1} onClick={handlePreviousPage} sx={{ minWidth: 'auto' }}>
          <NavigateBeforeIcon />
        </Button>
        {Array.from({ length: totalPages }, (_, index) => (
          <Button
            key={index}
            variant={currentPage === index + 1 ? 'contained' : 'outlined'}
            onClick={() => handlePageChange(index + 1)}
            sx={{ minWidth: 'auto' }}
          >
            {index + 1}
          </Button>
        ))}
        <Button variant="contained" disabled={currentPage === totalPages} onClick={handleNextPage} sx={{ minWidth: 'auto' }}>
            <NavigateNextIcon />
        </Button>
        <Button variant="contained" disabled={currentPage === totalPages} onClick={handleLastPage} sx={{ minWidth: 'auto' }}>
          <LastPageIcon />
        </Button>
      </Stack>
      <Typography variant="body2" align="center" sx={{ mt: 2 }}>
        第 {startRow} 条 到 第 {endRow} 条 , 共 {totalRows} 条 
      </Typography>
    </Box>
  );
};
