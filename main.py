from pydriller import Repository

issue_ids = ["CAMEL-180", "CAMEL-321", "CAMEL-1818", "CAMEL-3214", "CAMEL-18065"]
#repo_path = "https://github.com/apache/camel"
repo_path = "D:/WorkSpace/Python/camel"

unique_commits = set()
unique_files = set()
total_unit_size = 0.0
total_unit_complexity = 0.0
total_unit_interfacing = 0.0

for commit in Repository(repo_path,only_no_merge=True).traverse_commits():

    # filter commit message by issue id
    if any(issue_id in commit.msg for issue_id in issue_ids):

        # ensure unique commits
        if commit.hash not in unique_commits:
            unique_commits.add(commit.hash)

            # collect unique file names
            for file in commit.modified_files:
                if file.filename:
                    unique_files.add(file.filename)

            # collect dmm data
            total_unit_size += float(commit.dmm_unit_size or 0.0)
            total_unit_complexity += float(commit.dmm_unit_complexity or 0.0)
            total_unit_interfacing += float(commit.dmm_unit_interfacing or 0.0)


# Results
total_unique_commits = len(unique_commits)
total_unique_files = len(unique_files)
print("Total unique commits:", total_unique_commits)
print("Total unique files changed:", total_unique_files)
print(f"Average number of unique file changed :{total_unique_files/total_unique_commits:.2f}")
print(f"Total dmm_unit_size: {total_unit_size:.2f}   Average dmm_unit_size:{total_unit_size/total_unique_commits:.2f}" )
print(f"Total dmm_unit_complexity: {total_unit_complexity:.2f}   Average dmm_unit_complexity:{total_unit_complexity/total_unique_commits:.2f}")
print(f"Total dmm_unit_interfacing: {total_unit_interfacing:.2f}   Average dmm_unit_interfacing:{total_unit_interfacing/total_unique_commits:.2f}")

# Output
#Total unique commits: 169
#Total unique files changed: 603
#Average number of unique file changed :3.57
#Total dmm_unit_size: 65.22   Average dmm_unit_size:0.39
#Total dmm_unit_complexity: 76.11   Average dmm_unit_complexity:0.45
#Total dmm_unit_interfacing: 97.91   Average dmm_unit_interfacing:0.58

# Github repo link: https://github.com/wasimakram23/DSSE_PreAssignment