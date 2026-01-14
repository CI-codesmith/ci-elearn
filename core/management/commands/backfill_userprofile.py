from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import UserProfile, Role


class Command(BaseCommand):
    help = 'Safely backfill UserProfile for all existing Django Users (idempotent, safe to re-run)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be done without making changes',
        )

    def handle(self, *args, **options):
        dry_run = options.get('dry_run', False)
        
        # Get or create default Student role
        student_role, _ = Role.objects.get_or_create(
            name='Student',
            defaults={'description': 'Student - Default role for new users'}
        )
        
        # Get all Django Users
        users = User.objects.all()
        total_users = users.count()
        
        created_count = 0
        already_exist_count = 0
        
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(f"UserProfile Backfill Process")
        self.stdout.write(f"{'='*60}")
        self.stdout.write(f"Total Users: {total_users}")
        self.stdout.write(f"Dry Run: {dry_run}")
        self.stdout.write(f"{'='*60}\n")
        
        for user in users:
            # Check if profile already exists (safe pattern)
            profile = UserProfile.objects.filter(user=user).first()
            
            if profile:
                # Profile already exists
                already_exist_count += 1
                self.stdout.write(f"✓ {user.username} - Profile exists")
            else:
                # Profile missing - need to create
                if not dry_run:
                    profile = UserProfile.objects.create(user=user)
                    profile.roles.add(student_role)
                    created_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f"✓ {user.username} - Profile created with role: {student_role.name}")
                    )
                else:
                    created_count += 1
                    self.stdout.write(
                        self.style.WARNING(f"→ {user.username} - Would create profile with role: {student_role.name}")
                    )
        
        # Summary
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(f"Summary:")
        self.stdout.write(f"{'='*60}")
        self.stdout.write(self.style.SUCCESS(f"✓ Profiles Already Existed: {already_exist_count}"))
        
        if dry_run:
            self.stdout.write(self.style.WARNING(f"→ Would Create: {created_count}"))
            self.stdout.write(self.style.WARNING(f"\n(This was a dry run. Re-run without --dry-run to apply changes)"))
        else:
            self.stdout.write(self.style.SUCCESS(f"✓ Profiles Created: {created_count}"))
        
        self.stdout.write(f"✓ Total Processed: {total_users}")
        self.stdout.write(f"{'='*60}\n")
        
        if not dry_run and created_count > 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f"\n✓ Backfill complete! {created_count} UserProfile(s) created."
                )
            )
        elif dry_run:
            self.stdout.write(
                self.style.WARNING(
                    f"\n→ Preview complete. {created_count} profile(s) would be created."
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"\n✓ All users already have profiles! No changes needed."
                )
            )
