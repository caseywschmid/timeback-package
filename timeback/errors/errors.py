class TimebackError(Exception):
    """Base exception for Timeback client errors."""
    
    def __init__(self, message: str, error_details=None, **kwargs):
        super().__init__(message)
        self.error_details = error_details
        self._base_message = message
    
    def _format_error_message(self) -> str:
        """Format a unified error message with [TIMEBACK] prefix."""
        parts = ["[TIMEBACK]"]
        
        # Extract human-readable description from parsed error details
        if self.error_details and hasattr(self.error_details, 'imsx_description'):
            description = self.error_details.imsx_description
            parts.append(description)
            
            # Extract code minor details
            if hasattr(self.error_details, 'imsx_CodeMinor'):
                details = []
                for field in self.error_details.imsx_CodeMinor.imsx_codeMinorField:
                    details.append(f"{field.imsx_codeMinorFieldName}: {field.imsx_codeMinorFieldValue}")
                if details:
                    parts.append(f"Details: {', '.join(details)}")
            
            # Add request context from base message
            if self._base_message:
                parts.append(self._base_message)
        else:
            # Fallback to base message if no parsed details
            parts.append(self._base_message)
        
        return "\n".join(parts)
    
    def __str__(self) -> str:
        return self._format_error_message()


class ConfigurationError(TimebackError):
    """Raised when required configuration/env vars are missing or invalid."""
    def __init__(self, message: str, **kwargs):
        super().__init__(f"Configuration Error: {message}", **kwargs)


class AuthError(TimebackError):
    """Raised when authentication fails."""
    def __init__(self, message: str, error_details=None, **kwargs):
        super().__init__(f"Authentication Error: {message}", error_details=error_details, **kwargs)


class RequestError(TimebackError):
    """Raised for non-2xx HTTP responses not covered by more specific errors."""
    def __init__(self, message: str, error_details=None, **kwargs):
        super().__init__(f"Request Error: {message}", error_details=error_details, **kwargs)


class NotFoundError(RequestError):
    """Raised when a 404 is returned by the API."""
    def __init__(self, message: str, error_details=None, **kwargs):
        super().__init__(f"Resource Not Found: {message}", error_details=error_details, **kwargs)


class RateLimitError(RequestError):
    """Raised when a 429 is returned by the API."""
    def __init__(self, message: str, error_details=None, **kwargs):
        super().__init__(f"Rate Limit Exceeded: {message}", error_details=error_details, **kwargs)


class ServerError(RequestError):
    """Raised when a 5xx is returned by the API."""
    def __init__(self, message: str, error_details=None, **kwargs):
        super().__init__(f"Server Error: {message}", error_details=error_details, **kwargs)


class ParseError(TimebackError):
    """Raised when response parsing into models fails."""
    def __init__(self, message: str, **kwargs):
        super().__init__(f"Parse Error: {message}", **kwargs)


