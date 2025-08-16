import { render, screen } from '@testing-library/react';
import App from './App';

// The default CRA test looked for a "learn react" link which our
// application does not render.  This caused the test suite to fail.
// Update the test to assert that our main heading is present instead.
test('renders application heading', () => {
  render(<App />);
  const heading = screen.getByRole('heading', { name: /ai detection tool/i });
  expect(heading).toBeInTheDocument();
});
