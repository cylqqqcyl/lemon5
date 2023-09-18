import { alpha } from '@mui/material/styles';

const withAlphas = (color) => {
  return {
    ...color,
    alpha4: alpha(color.main, 0.04),
    alpha8: alpha(color.main, 0.08),
    alpha12: alpha(color.main, 0.12),
    alpha30: alpha(color.main, 0.30),
    alpha50: alpha(color.main, 0.50)
  };
};

export const neutral = {
  50: '#F3F9E3',
  100: '#F1F8DD',
  200: '#E5E7EB',
  300: '#D2D6DB',
  400: '#9DA4AE',
  500: '#6C737F',
  600: '#4D5761',
  700: '#2F3746',
  800: '#242124',
  900: '#111927'
};

export const citrine = withAlphas({
  lightest: '#F8F0B4',
  light: '#F3E57C',
  main: '#EDD83D',
  dark: '#E0C815',
  darkest: '#A89610',
  contrastText: '#242124'
});

export const success = withAlphas({
  lightest: '#B8DDA7',
  light: '#94CC7B',
  main: '#6AB547',
  dark: '#569339',
  darkest: '#3C6728',
  contrastText: '#F3F9E3'
});

export const info = withAlphas({
  lightest: '#C37E46',
  light: '#9A6E32',
  main: '#6B4423',
  dark: '#3E2714',
  darkest: '#0F0A05',
  contrastText: '#F3F9E3'
});

export const warning = withAlphas({
  lightest: '#FFFAEB',
  light: '#FEF0C7',
  main: '#F79009',
  dark: '#B54708',
  darkest: '#7A2E0E',
  contrastText: '#FFFFFF'
});

export const error = withAlphas({
  lightest: '#FEF3F2',
  light: '#FEE4E2',
  main: '#F04438',
  dark: '#B42318',
  darkest: '#7A271A',
  contrastText: '#FFFFFF'
});
