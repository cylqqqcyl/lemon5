import React, { useState, useRef } from 'react';
import { Box, Button, Stack, Typography } from '@mui/material';
import NavigateBeforeIcon from '@mui/icons-material/NavigateBefore';
import NavigateNextIcon from '@mui/icons-material/NavigateNext';
import FirstPageIcon from '@mui/icons-material/FirstPage';
import LastPageIcon from '@mui/icons-material/LastPage';
import { VoicesCard } from './voices-card';
import { voices, attributes } from './constants';

export const VoicesGrid = ({ onCardClick }) => {
    const [currentPage, setCurrentPage] = useState(1);
    const currentlyPlayingAudioRef = useRef(null); // Ref to hold the currently playing audio

    const rowsPerPage = 5;
    const totalRows = voices.length;
    const startRow = (currentPage - 1) * rowsPerPage + 1;
    const endRow = Math.min(currentPage * rowsPerPage, totalRows);
    const totalPages = Math.ceil(totalRows / rowsPerPage);

    const handlePageChange = (page) => {
        setCurrentPage(page);
    };

    const handleNextPage = () => {
        if (currentPage < totalPages) {
            setCurrentPage(prevPage => prevPage + 1);
        }
    };

    const handlePreviousPage = () => {
        if (currentPage > 1) {
            setCurrentPage(prevPage => prevPage - 1);
        }
    };

    const handleFirstPage = () => {
        setCurrentPage(1);
    };

    const handleLastPage = () => {
        setCurrentPage(totalPages);
    };

    return (
        <Box sx={{ p: 0, py: 2 }}>
            <Stack spacing={2}>
                {/* Rows */}
                {Array.from({ length: endRow - startRow + 1 }, (_, index) => (
                    <VoicesCard 
                        key={index} 
                        index={index + 1 + (currentPage - 1) * rowsPerPage}
                        attributes={attributes}
                        onClick={() => onCardClick && onCardClick(index + 1 + (currentPage - 1) * rowsPerPage)} 
                        playingAudioRef={currentlyPlayingAudioRef} // Pass the ref down
                    />
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
