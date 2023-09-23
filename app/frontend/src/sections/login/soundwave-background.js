import React, { useEffect, useRef } from 'react';
import { useTheme } from '@mui/material/styles';
import { Box } from '@mui/material';
import * as d3 from 'd3';

const SoundWaveBox = ({ children, ...rest }) => {
  const ref = useRef(null);
  const theme = useTheme();
  const fillColor = theme.palette.primary.main;

  useEffect(() => {

    if (ref.current) { // if the ref is defined then do the following

    let svg = d3.select(ref.current).select("svg#soundWaveSvg");
    const padding = 10;

    if (svg.empty()) {
      svg = d3.select(ref.current)
        .append("svg")
        .attr("id", "soundWaveSvg")
        .attr("width", "100%")
        .attr("height", "100%")
        .attr("viewBox", `0 0 ${ref.current.clientWidth*2} ${ref.current.clientHeight*2}`);
    }

    const barWidth = 10;
    const barSpacing = 2; // space between bars
    const numBars = Math.floor(2*ref.current.clientWidth / (barWidth + barSpacing));

    let bars = d3.range(0, numBars).map((_, i) => 
    100);

    svg.selectAll("rect")
        .data(bars)
        .join("rect")
        .attr("x", (d, i) => i * (barWidth + barSpacing))
        .attr("y", d => (ref.current.clientHeight / 2) - d/2)
        .attr("width", barWidth)
        .attr("height", d => d)
        .attr("fill", fillColor);

    const updateBars = () => {

      bars = bars.map((bar) => Math.min(Math.max(Math.random() * 30-15 +bar,0),ref.current.clientHeight-30));

      svg.selectAll("rect")
        .data(bars)
        .transition()
        .duration(100)
        .attr("y", d => (ref.current.clientHeight / 2) - d/2-20)
        .attr("height", d => d);
    };

    const timer = d3.interval(updateBars, 100);

    return () => timer.stop();

    }
  }, []);

  return (
    <Box ref={ref} {...rest}>
      {children}
    </Box>
  );
};

export default SoundWaveBox;
