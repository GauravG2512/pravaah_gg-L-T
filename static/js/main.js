document.addEventListener('DOMContentLoaded', () => {
    // Theme Management
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn ? themeToggleBtn.querySelector('i') : null;
    
    // Check for saved theme preference or system preference
    const savedTheme = localStorage.getItem('theme') || 'dark'; // default to dark
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
            
            // Create soft visual notification for theme change
            createToast(`Switched to ${newTheme} mode!`, 'info');
        });
    }

    function updateThemeIcon(theme) {
        if (!themeIcon) return;
        if (theme === 'light') {
            themeIcon.className = 'fas fa-moon';
            themeToggleBtn.title = 'Switch to Dark Mode';
        } else {
            themeIcon.className = 'fas fa-sun';
            themeToggleBtn.title = 'Switch to Light Mode';
        }
    }

    // Sidebar Responsiveness & Collapsing
    const sidebar = document.getElementById('sidebar');
    const sidebarToggleBtn = document.getElementById('sidebar-toggle');
    
    if (sidebarToggleBtn && sidebar) {
        sidebarToggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (window.innerWidth > 991) {
                // Desktop: Collapse sidebar
                sidebar.classList.toggle('collapsed');
                // Save collapsed state
                localStorage.setItem('sidebar-collapsed', sidebar.classList.contains('collapsed'));
            } else {
                // Mobile: Open/Close Drawer sidebar
                sidebar.classList.toggle('mobile-show');
            }
        });
        
        // Restore Desktop Sidebar collapsed state
        const isCollapsed = localStorage.getItem('sidebar-collapsed') === 'true';
        if (isCollapsed && window.innerWidth > 991) {
            sidebar.classList.add('collapsed');
        }
    }

    // User Profile Dropdown
    const profileTrigger = document.getElementById('profile-trigger');
    const profileDropdown = document.getElementById('profile-dropdown');
    
    if (profileTrigger && profileDropdown) {
        profileTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            profileDropdown.classList.toggle('show');
        });
    }

    // Close elements when clicking outside
    document.addEventListener('click', (e) => {
        // Dropdown outside click
        if (profileDropdown && profileDropdown.classList.contains('show') && !profileTrigger.contains(e.target)) {
            profileDropdown.classList.remove('show');
        }
        
        // Mobile Sidebar outside click
        if (sidebar && sidebar.classList.contains('mobile-show') && !sidebar.contains(e.target) && e.target !== sidebarToggleBtn) {
            sidebar.classList.remove('mobile-show');
        }
    });

    // Dynamic Toast Auto-Dismissal
    const toasts = document.querySelectorAll('.glass-toast');
    toasts.forEach(toast => {
        setupToast(toast);
    });

    function setupToast(toast) {
        const closeBtn = toast.querySelector('.toast-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                dismissToast(toast);
            });
        }
        // Auto dismiss after 5 seconds
        setTimeout(() => {
            dismissToast(toast);
        }, 5000);
    }

    function dismissToast(toast) {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(10px) scale(0.95)';
        toast.style.transition = 'all 0.3s ease';
        setTimeout(() => {
            toast.remove();
        }, 300);
    }

    // Programmatic Toast creator
    function createToast(message, type = 'success') {
        let container = document.querySelector('.toast-container');
        if (!container) {
            container = document.createElement('div');
            container.className = 'toast-container';
            document.body.appendChild(container);
        }

        const toast = document.createElement('div');
        toast.className = `glass-toast glass-panel toast-${type}`;
        
        let iconClass = 'fa-check-circle';
        if (type === 'error') iconClass = 'fa-times-circle';
        if (type === 'info') iconClass = 'fa-info-circle';
        if (type === 'warning') iconClass = 'fa-exclamation-circle';

        toast.innerHTML = `
            <div class="toast-icon"><i class="fas ${iconClass}"></i></div>
            <div class="toast-content">${message}</div>
            <button class="toast-close"><i class="fas fa-times"></i></button>
        `;

        container.appendChild(toast);
        setupToast(toast);
    }
});
